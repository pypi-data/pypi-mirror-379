"""
Claude Code provider implementation for BAML
"""

from typing import Dict, Any, Optional
from .client import ClaudeCodeClient
from .error import ClaudeCodeError


class ClaudeCodeProvider:
    """BAML provider for Claude Code"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.client = ClaudeCodeClient(**config)
    
    
    def create_client(self) -> ClaudeCodeClient:
        """Create a Claude Code client"""
        return self.client
    
    def validate_config(self) -> bool:
        """Validate the provider configuration"""
        try:
            # Check if Claude Code CLI is available
            if not self.client.check_availability():
                raise ClaudeCodeError("Claude Code CLI is not available")
            
            # Validate required fields
            if not self.config.get("model"):
                raise ClaudeCodeError("Model is required")
            
            return True
        except Exception as e:
            raise ClaudeCodeError(f"Configuration validation failed: {str(e)}")
    
    def get_supported_features(self) -> Dict[str, bool]:
        """Get supported features"""
        return {
            "subagents": True,
            "hooks": True,
            "slash_commands": True,
            "memory_files": True,
            "realtime_streaming": True,
            "enhanced_metadata": True,
            "custom_auth": True,
            "cloudplan": True,
            "api_key": True,
        }


