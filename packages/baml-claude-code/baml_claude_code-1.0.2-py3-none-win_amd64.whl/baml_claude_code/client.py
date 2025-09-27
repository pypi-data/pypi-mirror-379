"""
Claude Code client implementation for Python
"""

import asyncio
import subprocess
import json
import os
from typing import Dict, List, Optional, Any, Union
from pathlib import Path

from .error import ClaudeCodeError


class ClaudeCodeClient:
    """Claude Code client for BAML"""
    
    def __init__(
        self,
        model: str = "sonnet",
        api_key: Optional[str] = None,
        claude_binary: Optional[str] = None,
        **kwargs
    ):
        self.model = model
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.claude_binary = claude_binary or "claude"
        self.options = kwargs
        
    async def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> str:
        """Generate a response using Claude Code"""
        try:
            # Build command arguments
            args = [self.claude_binary, "code", "--model", self.model]
            
            if self.api_key:
                args.extend(["--api-key", self.api_key])
            
            if max_tokens:
                args.extend(["--max-tokens", str(max_tokens)])
                
            if temperature:
                args.extend(["--temperature", str(temperature)])
            
            # Add custom options
            for key, value in kwargs.items():
                if value is not None:
                    args.extend([f"--{key.replace('_', '-')}", str(value)])
            
            # Add prompt
            args.append(prompt)
            
            # Execute command
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                raise ClaudeCodeError(f"Claude Code execution failed: {stderr.decode()}")
            
            return stdout.decode().strip()
            
        except Exception as e:
            raise ClaudeCodeError(f"Failed to generate response: {str(e)}")
    
    def generate_sync(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> str:
        """Synchronous version of generate"""
        return asyncio.run(self.generate(prompt, max_tokens, temperature, **kwargs))
    
    def check_availability(self) -> bool:
        """Check if Claude Code CLI is available"""
        try:
            result = subprocess.run(
                [self.claude_binary, "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            return False
    
    def get_version(self) -> Optional[str]:
        """Get Claude Code version"""
        try:
            result = subprocess.run(
                [self.claude_binary, "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return result.stdout.strip()
            return None
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            return None


