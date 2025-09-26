"""
AI大模型请求客户端

提供统一的AI大模型调用接口，支持多种模型和验证机制。
"""

import requests
import json
import time
from typing import Dict, Any, Optional, Callable, Union
from dataclasses import dataclass
from rich.console import Console
from .config import AIConfig, AIModelConfig
from .validators import ResponseValidator

# 创建console实例用于调试日志
console = Console()


@dataclass
class AIRequest:
    """AI请求数据结构"""
    messages: list
    model: Optional[str] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    stream: bool = False
    extra_params: Optional[Dict[str, Any]] = None


@dataclass
class AIResponse:
    """AI响应数据结构"""
    content: str
    raw_response: Dict[str, Any]
    model: str
    usage: Optional[Dict[str, Any]] = None
    finish_reason: Optional[str] = None
    request_id: Optional[str] = None


class AIClient:
    """AI大模型请求客户端"""
    
    def __init__(self, config_path: str = None, model_name: str = None, system_prompt: str = None):
        """
        初始化AI客户端
        
        Args:
            config_path: 配置文件路径
            model_name: 模型名称，如果为None则使用默认模型
            system_prompt: 系统提示词，将在每次对话开始时自动添加
        """
        self.config_manager = AIConfig(config_path)
        self.model_name = model_name or self.config_manager.get_default_model()
        self.model_config = self.config_manager.get_model_config(self.model_name)
        self.system_prompt = system_prompt
        self.session = requests.Session()
        
        # 设置默认请求头
        if self.model_config.headers:
            self.session.headers.update(self.model_config.headers)
        
        # 设置认证
        self._setup_auth()
    
    def _setup_auth(self):
        """设置认证信息"""
        if self.model_config.api_key:
            if 'openai' in self.model_name.lower():
                self.session.headers['Authorization'] = f'Bearer {self.model_config.api_key}'
            elif 'claude' in self.model_name.lower() or 'anthropic' in self.model_name.lower():
                self.session.headers['x-api-key'] = self.model_config.api_key
            else:
                # 通用认证方式
                self.session.headers['Authorization'] = f'Bearer {self.model_config.api_key}'
    
    def _prepare_request_data(self, request: AIRequest) -> Dict[str, Any]:
        """
        准备请求数据
        
        Args:
            request: AI请求对象
            
        Returns:
            Dict: 请求数据
        """
        data = {
            'model': request.model or self.model_config.model,
            'max_tokens': request.max_tokens or self.model_config.max_tokens,
            'temperature': request.temperature or self.model_config.temperature,
        }
        
        # 根据不同的模型类型处理消息格式
        if 'openai' in self.model_name.lower():
            data['messages'] = request.messages
            if request.stream:
                data['stream'] = True
        elif 'claude' in self.model_name.lower() or 'anthropic' in self.model_name.lower():
            # Claude API格式
            if request.messages:
                # 转换消息格式
                if len(request.messages) == 1 and request.messages[0].get('role') == 'user':
                    data['messages'] = request.messages
                else:
                    data['messages'] = request.messages
        elif 'qwen' in self.model_name.lower():
            # Qwen API格式
            data['messages'] = request.messages
            if request.stream:
                data['stream'] = True
        else:
            # 通用格式
            data['messages'] = request.messages
            if request.stream:
                data['stream'] = True
        
        # 添加额外参数
        if request.extra_params:
            data.update(request.extra_params)
        
        if self.model_config.extra_params:
            data.update(self.model_config.extra_params)        
        return data
    
    def _parse_response(self, response: requests.Response) -> AIResponse:
        """
        解析响应数据
        
        Args:
            response: HTTP响应对象
            
        Returns:
            AIResponse: 解析后的AI响应对象
        """
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            raise Exception(f"无法解析响应JSON: {response.text}")
        
        # 根据不同模型解析响应
        if 'openai' in self.model_name.lower():
            return self._parse_openai_response(response_data)
        elif 'claude' in self.model_name.lower() or 'anthropic' in self.model_name.lower():
            return self._parse_claude_response(response_data)
        else:
            return self._parse_generic_response(response_data)
    
    def _parse_openai_response(self, data: Dict[str, Any]) -> AIResponse:
        """解析OpenAI响应"""
        if 'choices' not in data or not data['choices']:
            raise Exception("OpenAI响应中没有choices字段")
        
        choice = data['choices'][0]
        content = choice.get('message', {}).get('content', '')
        finish_reason = choice.get('finish_reason')
        
        return AIResponse(
            content=content,
            raw_response=data,
            model=data.get('model', self.model_config.model),
            usage=data.get('usage'),
            finish_reason=finish_reason,
            request_id=data.get('id')
        )
    
    def _parse_claude_response(self, data: Dict[str, Any]) -> AIResponse:
        """解析Claude响应"""
        if 'content' not in data:
            raise Exception("Claude响应中没有content字段")
        
        content_list = data['content']
        if isinstance(content_list, list) and content_list:
            content = content_list[0].get('text', '')
        else:
            content = str(content_list)
        
        return AIResponse(
            content=content,
            raw_response=data,
            model=data.get('model', self.model_config.model),
            usage=data.get('usage'),
            finish_reason=data.get('stop_reason'),
            request_id=data.get('id')
        )
    
    def _parse_generic_response(self, data: Dict[str, Any]) -> AIResponse:
        """解析通用响应"""
        content = ''
        finish_reason = None
        
        # 首先尝试OpenAI格式 (choices[0].message.content)
        if 'choices' in data and data['choices'] and len(data['choices']) > 0:
            choice = data['choices'][0]
            if 'message' in choice and 'content' in choice['message']:
                content = choice['message']['content']
                finish_reason = choice.get('finish_reason')
        
        # 如果没有找到，尝试其他可能的内容字段
        if not content:
            for field in ['content', 'text', 'response', 'output']:
                if field in data:
                    content = str(data[field])
                    break
        
        return AIResponse(
            content=content,
            raw_response=data,
            model=data.get('model', self.model_config.model),
            usage=data.get('usage'),
            finish_reason=finish_reason or data.get('finish_reason'),
            request_id=data.get('id')
        )
    
    def chat(self, 
             messages: Union[str, list], 
             model: str = None,
             max_tokens: int = None,
             temperature: float = None,
             validator: ResponseValidator = None,
             callback: Callable[[AIResponse], Any] = None,
             **kwargs) -> AIResponse:
        """
        发送聊天请求
        
        Args:
            messages: 消息内容，可以是字符串或消息列表
            model: 模型名称
            max_tokens: 最大token数
            temperature: 温度参数
            validator: 响应验证器
            callback: 响应回调函数
            **kwargs: 其他参数
            
        Returns:
            AIResponse: AI响应对象
        """

        # 处理消息格式
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        
        # 如果设置了系统提示词，且消息列表中没有系统消息，则添加系统提示词
        if self.system_prompt:
            if not messages or messages[0].get("role") != "system":
                messages.insert(0, {"role": "system", "content": self.system_prompt})
        
        
        # 创建请求对象
        request = AIRequest(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            extra_params=kwargs
        )
        
        return self.send_request(request, validator, callback)
    
    def send_request(self, 
                    request: AIRequest, 
                    validator: ResponseValidator = None,
                    callback: Callable[[AIResponse], Any] = None) -> AIResponse:
        """
        发送AI请求
        
        Args:
            request: AI请求对象
            validator: 响应验证器
            callback: 响应回调函数
            
        Returns:
            AIResponse: AI响应对象
        """
        
        try:
            # 准备请求数据
            request_data = self._prepare_request_data(request)
            
            response = self.session.post(
                self.model_config.endpoint,
                json=request_data,
                timeout=self.model_config.timeout
            )

            # 检查HTTP状态
            if not response.ok:
                console.print(f"[bold red][DEBUG][/bold red] HTTP请求失败: {response.status_code}")
                console.print(f"[bold red][DEBUG][/bold red] 错误响应内容: {response.text[:500]}...")
                raise Exception(f"HTTP请求失败: {response.status_code} - {response.text}")
            
            
            # 解析响应
            ai_response = self._parse_response(response)
            
            # 验证响应
            if validator:
                is_valid, errors = validator.validate(ai_response.raw_response)
                if not is_valid:
                    raise Exception(f"响应验证失败: {'; '.join(errors)}")
            
            # 执行回调
            if callback:
                callback(ai_response)
            
            return ai_response
            
        except requests.exceptions.Timeout:
            raise Exception(f"请求超时 ({self.model_config.timeout}秒)")
        except requests.exceptions.ConnectionError:
            raise Exception("连接错误，请检查网络和端点地址")
        except Exception as e:
            console.print(f"[bold red][DEBUG][/bold red] 请求异常: {type(e).__name__}: {e}")
            raise Exception(f"AI请求失败: {e}")
    
    def stream_chat(self, 
                   messages: Union[str, list],
                   model: str = None,
                   max_tokens: int = None,
                   temperature: float = None,
                   callback: Callable[[str], None] = None,
                   **kwargs):
        """
        流式聊天请求
        
        Args:
            messages: 消息内容
            model: 模型名称
            max_tokens: 最大token数
            temperature: 温度参数
            callback: 流式数据回调函数
            **kwargs: 其他参数
            
        Yields:
            str: 流式响应内容片段
        """
        
        # 处理消息格式
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        
        
        # 如果设置了系统提示词，且消息列表中没有系统消息，则添加系统提示词
        if self.system_prompt and (not messages or messages[0].get("role") != "system"):
            messages.insert(0, {"role": "system", "content": self.system_prompt})

        # 创建请求对象
        request = AIRequest(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
            extra_params=kwargs
        )
        
        try:
            
            # 准备请求数据
            request_data = self._prepare_request_data(request)
            
            # 发送流式请求
            start_time = time.time()
            
            response = self.session.post(
                self.model_config.endpoint,
                json=request_data,
                timeout=self.model_config.timeout,
                stream=True
            )
            
            
            # 检查HTTP状态
            if not response.ok:
                console.print(f"[bold red][DEBUG][/bold red] 错误响应内容: {response.text[:500]}...")
                raise Exception(f"HTTP请求失败: {response.status_code} - {response.text}")
            
            chunk_count = 0
            
            # 处理流式响应
            for line in response.iter_lines():
                if line:
                    line_text = line.decode('utf-8')
                    
                    if line_text.startswith('data: '):
                        data_text = line_text[6:]
                        
                        if data_text.strip() == '[DONE]':
                            break
                        
                        try:
                            data = json.loads(data_text)
                            content = self._extract_stream_content(data)
                            if content:
                                chunk_count += 1
                                if callback:
                                    callback(content)
                                yield content
                        except json.JSONDecodeError:
                            console.print(f"[bold yellow][DEBUG][/bold yellow] 跳过无效的JSON数据: {data_text[:100]}...")
                            continue
            
        except requests.exceptions.Timeout:
            console.print(f"[bold red][DEBUG][/bold red] 流式请求超时异常")
            raise Exception(f"请求超时 ({self.model_config.timeout}秒)")
        except requests.exceptions.ConnectionError:
            console.print(f"[bold red][DEBUG][/bold red] 流式请求连接错误异常")
            raise Exception("连接错误，请检查网络和端点地址")
        except Exception as e:
            console.print(f"[bold red][DEBUG][/bold red] 流式请求异常: {type(e).__name__}: {e}")
            raise Exception(f"流式请求失败: {e}")
    
    def _extract_stream_content(self, data: Dict[str, Any]) -> str:
        """从流式数据中提取内容"""
        if 'openai' in self.model_name.lower():
            choices = data.get('choices', [])
            if choices:
                delta = choices[0].get('delta', {})
                return delta.get('content', '')
        elif 'claude' in self.model_name.lower():
            return data.get('delta', {}).get('text', '')
        elif 'qwen' in self.model_name.lower():
            # 处理qwen模型的流式响应格式
            # 尝试多种可能的格式
            
            # 格式1: choices[0].delta.content (类似OpenAI)
            choices = data.get('choices', [])
            if choices:
                delta = choices[0].get('delta', {})
                content = delta.get('content', '')
                if content:
                    return content
            
            # 格式2: 直接的content字段
            content = data.get('content', '')
            if content:
                return content
            
            # 格式3: text字段
            content = data.get('text', '')
            if content:
                return content
            
            # 格式4: output字段
            content = data.get('output', '')
            if content:
                return content
        
        return ''
    
    def switch_model(self, model_name: str):
        """
        切换模型
        
        Args:
            model_name: 新的模型名称
        """
        self.model_name = model_name
        self.model_config = self.config_manager.get_model_config(model_name)
        
        # 重新设置认证
        self.session.headers.clear()
        if self.model_config.headers:
            self.session.headers.update(self.model_config.headers)
        self._setup_auth()
    
    def get_available_models(self) -> list:
        """获取可用的模型列表"""
        return self.config_manager.list_models()
    
    def get_current_model(self) -> str:
        """获取当前使用的模型"""
        return self.model_name