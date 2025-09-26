#!/usr/bin/env python3
"""
Advanced Configuration Builder for MCP Proxy Adapter
Creates configurations from scratch based on protocol, authentication, and other parameters.

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""
import json
import uuid
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from enum import Enum


class Protocol(Enum):
    """Supported protocols."""
    HTTP = "http"
    HTTPS = "https"
    MTLS = "mtls"


class AuthMethod(Enum):
    """Supported authentication methods."""
    NONE = "none"
    TOKEN = "token"
    BASIC = "basic"


class ConfigBuilder:
    """Advanced configuration builder for MCP Proxy Adapter."""
    
    def __init__(self):
        """Initialize the configuration builder."""
        self.config = {}
        self._reset_to_defaults()
    
    def _reset_to_defaults(self):
        """Reset configuration to default values."""
        self.config = {
            "uuid": str(uuid.uuid4()),
            "server": {
                "host": "0.0.0.0",
                "port": 8000,
                "debug": False,
                "log_level": "INFO"
            },
            "logging": {
                "level": "INFO",
                "file": None,
                "log_dir": "./logs",
                "log_file": "mcp_proxy_adapter.log",
                "error_log_file": "mcp_proxy_adapter_error.log",
                "access_log_file": "mcp_proxy_adapter_access.log",
                "max_file_size": "10MB",
                "backup_count": 5,
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "date_format": "%Y-%m-%d %H:%M:%S",
                "console_output": True,
                "file_output": True
            },
            "commands": {
                "auto_discovery": True,
                "commands_directory": "./commands",
                "catalog_directory": "./catalog",
                "plugin_servers": [],
                "auto_install_dependencies": True,
                "enabled_commands": [
                    "health",
                    "echo",
                    "list",
                    "help"
                ],
                "disabled_commands": [],
                "custom_commands_path": "./commands"
            },
            "ssl": {
                "enabled": False,
                "mode": "https_only",
                "cert_file": None,
                "key_file": None,
                "ca_cert": None,
                "verify_client": False,
                "client_cert_required": False,
                "cipher_suites": [
                    "TLS_AES_256_GCM_SHA384",
                    "TLS_CHACHA20_POLY1305_SHA256"
                ],
                "min_tls_version": "TLSv1.2",
                "max_tls_version": None
            },
            "transport": {
                "type": "http",
                "port": None,
                "ssl": {
                    "enabled": False,
                    "cert_file": None,
                    "key_file": None,
                    "ca_cert": None,
                    "verify_client": False,
                    "client_cert_required": False
                }
            },
            "proxy_registration": {
                "enabled": False,
                "auth_method": "token",
                "server_url": None,
                "proxy_url": None,
                "fallback_proxy_url": None,
                "ssl": {
                    "ca_cert": None,
                    "verify_mode": "CERT_REQUIRED"
                },
                "heartbeat": {
                    "enabled": True,
                    "interval": 30,
                    "timeout": 10
                },
                "server_id": "mcp_proxy_adapter",
                "server_name": "MCP Proxy Adapter",
                "description": "MCP Proxy Adapter Server",
                "version": "1.0.0",
                "capabilities": ["jsonrpc", "rest", "health"],
                "endpoints": {
                    "jsonrpc": "/api/jsonrpc",
                    "rest": "/cmd",
                    "health": "/health"
                },
                "auth": {
                    "token": None
                }
            },
            "debug": {
                "enabled": False,
                "log_level": "DEBUG",
                "trace_requests": False,
                "trace_responses": False
            },
            "security": {
                "framework": "mcp_security_framework",
                "enabled": False,
                "debug": False,
                "environment": "dev",
                "version": "1.0.0",
                "auth": {
                    "enabled": False,
                    "methods": ["api_key"],
                    "api_keys": {},
                    "user_roles": {},
                    "jwt_secret": "",
                    "jwt_algorithm": "HS256",
                    "jwt_expiry_hours": 24,
                    "certificate_auth": False,
                    "certificate_roles_oid": "1.3.6.1.4.1.99999.1.1",
                    "certificate_permissions_oid": "1.3.6.1.4.1.99999.1.2",
                    "basic_auth": False,
                    "oauth2_config": None,
                    "public_paths": ["/health", "/docs", "/openapi.json"],
                    "security_headers": None
                },
                "ssl": {
                    "enabled": False,
                    "cert_file": None,
                    "key_file": None,
                    "ca_cert_file": None,
                    "client_cert_file": None,
                    "client_key_file": None,
                    "verify_mode": "CERT_NONE",
                    "min_tls_version": "TLSv1.2",
                    "max_tls_version": None,
                    "cipher_suite": None,
                    "check_hostname": True,
                    "check_expiry": True,
                    "expiry_warning_days": 30
                },
                "certificates": {
                    "enabled": False,
                    "ca_cert_path": None,
                    "ca_key_path": None,
                    "cert_storage_path": "./certs",
                    "key_storage_path": "./keys",
                    "default_validity_days": 365,
                    "key_size": 2048,
                    "hash_algorithm": "sha256",
                    "crl_enabled": False,
                    "crl_path": None,
                    "crl_url": None,
                    "crl_validity_days": 30,
                    "auto_renewal": False,
                    "renewal_threshold_days": 30
                },
                "permissions": {
                    "enabled": False,
                    "roles_file": None,
                    "default_role": "guest",
                    "admin_role": "admin",
                    "role_hierarchy": {},
                    "permission_cache_enabled": False,
                    "permission_cache_ttl": 300,
                    "wildcard_permissions": False,
                    "strict_mode": False,
                    "roles": None
                },
                "rate_limit": {
                    "enabled": False,
                    "default_requests_per_minute": 60,
                    "default_requests_per_hour": 1000,
                    "burst_limit": 2,
                    "window_size_seconds": 60,
                    "storage_backend": "memory",
                    "redis_config": None,
                    "cleanup_interval": 300,
                    "exempt_paths": ["/health", "/docs", "/openapi.json"],
                    "exempt_roles": ["admin"]
                },
                "logging": {
                    "enabled": True,
                    "level": "INFO",
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    "date_format": "%Y-%m-%d %H:%M:%S",
                    "file_path": None,
                    "max_file_size": 10,
                    "backup_count": 5,
                    "console_output": True,
                    "json_format": False,
                    "include_timestamp": True,
                    "include_level": True,
                    "include_module": True
                }
            },
            "protocols": {
                "enabled": True,
                "allowed_protocols": ["http"],
                "default_protocol": "http",
                "protocol_handlers": {
                    "http": {
                        "enabled": True,
                        "port": None,
                        "ssl": False
                    },
                    "https": {
                        "enabled": False,
                        "port": None,
                        "ssl": True
                    },
                    "mtls": {
                        "enabled": False,
                        "port": None,
                        "ssl": True,
                        "client_cert_required": True
                    }
                }
            },
            "roles": {
                "enabled": False,
                "config_file": None,
                "default_policy": {
                    "deny_by_default": False,
                    "require_role_match": False,
                    "case_sensitive": False,
                    "allow_wildcard": False
                },
                "auto_load": False,
                "validation_enabled": False
            }
        }
    
    def set_server(self, host: str = "0.0.0.0", port: int = 8000, debug: bool = False, log_level: str = "INFO"):
        """Set server configuration."""
        self.config["server"] = {
            "host": host,
            "port": port,
            "debug": debug,
            "log_level": log_level
        }
        return self
    
    def set_logging(self, log_dir: str = "./logs", level: str = "INFO", console_output: bool = True, file_output: bool = True):
        """Set logging configuration."""
        self.config["logging"].update({
            "level": level,
            "log_dir": log_dir,
            "console_output": console_output,
            "file_output": file_output
        })
        return self
    
    def set_protocol(self, protocol: Protocol, cert_dir: str = "./certs", key_dir: str = "./keys"):
        """Set protocol configuration (HTTP, HTTPS, or mTLS)."""
        if protocol == Protocol.HTTP:
            self.config["ssl"]["enabled"] = False
            self.config["security"]["ssl"]["enabled"] = False
            self.config["protocols"]["allowed_protocols"] = ["http"]
            self.config["protocols"]["default_protocol"] = "http"
            self.config["protocols"]["protocol_handlers"]["http"]["enabled"] = True
            self.config["protocols"]["protocol_handlers"]["https"]["enabled"] = False
            self.config["protocols"]["protocol_handlers"]["mtls"]["enabled"] = False
            
        elif protocol == Protocol.HTTPS:
            self.config["ssl"]["enabled"] = True
            self.config["ssl"]["cert_file"] = f"{cert_dir}/server_cert.pem"
            self.config["ssl"]["key_file"] = f"{key_dir}/server_key.pem"
            self.config["ssl"]["ca_cert"] = f"{cert_dir}/ca_cert.pem"
            
            self.config["security"]["ssl"]["enabled"] = True
            self.config["security"]["ssl"]["cert_file"] = f"{cert_dir}/server_cert.pem"
            self.config["security"]["ssl"]["key_file"] = f"{key_dir}/server_key.pem"
            self.config["security"]["ssl"]["ca_cert_file"] = f"{cert_dir}/ca_cert.pem"
            
            self.config["protocols"]["allowed_protocols"] = ["https"]
            self.config["protocols"]["default_protocol"] = "https"
            self.config["protocols"]["protocol_handlers"]["http"]["enabled"] = False
            self.config["protocols"]["protocol_handlers"]["https"]["enabled"] = True
            self.config["protocols"]["protocol_handlers"]["mtls"]["enabled"] = False
            
        elif protocol == Protocol.MTLS:
            self.config["ssl"]["enabled"] = True
            self.config["ssl"]["cert_file"] = f"{cert_dir}/server_cert.pem"
            self.config["ssl"]["key_file"] = f"{key_dir}/server_key.pem"
            self.config["ssl"]["ca_cert"] = f"{cert_dir}/ca_cert.pem"
            self.config["ssl"]["verify_client"] = True
            self.config["ssl"]["client_cert_required"] = True
            
            self.config["security"]["ssl"]["enabled"] = True
            self.config["security"]["ssl"]["cert_file"] = f"{cert_dir}/server_cert.pem"
            self.config["security"]["ssl"]["key_file"] = f"{key_dir}/server_key.pem"
            self.config["security"]["ssl"]["ca_cert_file"] = f"{cert_dir}/ca_cert.pem"
            self.config["security"]["ssl"]["client_cert_file"] = f"{cert_dir}/admin_cert.pem"
            self.config["security"]["ssl"]["client_key_file"] = f"{key_dir}/admin_key.pem"
            self.config["security"]["ssl"]["verify_mode"] = "CERT_REQUIRED"
            
            self.config["protocols"]["allowed_protocols"] = ["mtls"]
            self.config["protocols"]["default_protocol"] = "mtls"
            self.config["protocols"]["protocol_handlers"]["http"]["enabled"] = False
            self.config["protocols"]["protocol_handlers"]["https"]["enabled"] = False
            self.config["protocols"]["protocol_handlers"]["mtls"]["enabled"] = True
            self.config["protocols"]["protocol_handlers"]["mtls"]["client_cert_required"] = True
        
        return self
    
    def set_auth(self, auth_method: AuthMethod, api_keys: Optional[Dict[str, str]] = None, roles: Optional[Dict[str, List[str]]] = None):
        """Set authentication configuration."""
        if auth_method == AuthMethod.NONE:
            self.config["security"]["enabled"] = False
            self.config["security"]["auth"]["enabled"] = False
            
        elif auth_method == AuthMethod.TOKEN:
            self.config["security"]["enabled"] = True
            self.config["security"]["auth"]["enabled"] = True
            self.config["security"]["auth"]["methods"] = ["api_key"]
            self.config["security"]["auth"]["api_keys"] = api_keys or {
                "admin": "admin-secret-key",
                "user": "user-secret-key"
            }
            
        elif auth_method == AuthMethod.BASIC:
            self.config["security"]["enabled"] = True
            self.config["security"]["auth"]["enabled"] = True
            self.config["security"]["auth"]["methods"] = ["basic_auth"]
            self.config["security"]["auth"]["basic_auth"] = True
        
        # Set roles if provided
        if roles:
            self.config["security"]["auth"]["user_roles"] = roles
            self.config["roles"]["enabled"] = True
            self.config["security"]["permissions"]["enabled"] = True
        
        return self
    
    def set_proxy_registration(self, enabled: bool = True, proxy_url: str = "https://127.0.0.1:20005", 
                             server_id: str = "mcp_proxy_adapter", cert_dir: str = "./certs"):
        """Set proxy registration configuration."""
        self.config["proxy_registration"]["enabled"] = enabled
        if enabled:
            self.config["proxy_registration"]["server_url"] = f"{proxy_url}/register"
            self.config["proxy_registration"]["proxy_url"] = proxy_url
            self.config["proxy_registration"]["fallback_proxy_url"] = proxy_url.replace("https://", "http://")
            self.config["proxy_registration"]["ssl"]["ca_cert"] = f"{cert_dir}/ca_cert.pem"
            self.config["proxy_registration"]["server_id"] = server_id
            self.config["proxy_registration"]["server_name"] = f"{server_id.title()} Server"
            self.config["proxy_registration"]["description"] = f"Test server for {server_id}"
        
        return self
    
    def set_debug(self, enabled: bool = False, log_level: str = "DEBUG"):
        """Set debug configuration."""
        self.config["debug"]["enabled"] = enabled
        self.config["debug"]["log_level"] = log_level
        if enabled:
            self.config["logging"]["level"] = log_level
        
        return self
    
    def set_commands(self, enabled_commands: Optional[List[str]] = None, disabled_commands: Optional[List[str]] = None):
        """Set commands configuration."""
        if enabled_commands:
            self.config["commands"]["enabled_commands"] = enabled_commands
        if disabled_commands:
            self.config["commands"]["disabled_commands"] = disabled_commands
        
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build and return the final configuration."""
        return self.config.copy()
    
    def save(self, file_path: Union[str, Path]) -> Path:
        """Save configuration to file."""
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
        
        return file_path
    
    def reset(self):
        """Reset configuration to defaults."""
        self._reset_to_defaults()
        return self


class ConfigFactory:
    """Factory for creating common configuration combinations."""
    
    @staticmethod
    def create_http_simple(host: str = "0.0.0.0", port: int = 20020, log_dir: str = "./logs") -> Dict[str, Any]:
        """Create simple HTTP configuration."""
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.HTTP)
                .set_auth(AuthMethod.NONE)
                .set_proxy_registration(enabled=False)
                .build())
    
    @staticmethod
    def create_http_token(host: str = "0.0.0.0", port: int = 20021, log_dir: str = "./logs", 
                         api_keys: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Create HTTP configuration with token authentication."""
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.HTTP)
                .set_auth(AuthMethod.TOKEN, api_keys=api_keys)
                .set_proxy_registration(enabled=False)
                .build())
    
    @staticmethod
    def create_https_simple(host: str = "0.0.0.0", port: int = 20022, log_dir: str = "./logs", 
                           cert_dir: str = "./certs", key_dir: str = "./keys") -> Dict[str, Any]:
        """Create simple HTTPS configuration."""
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.HTTPS, cert_dir=cert_dir, key_dir=key_dir)
                .set_auth(AuthMethod.NONE)
                .set_proxy_registration(enabled=False)
                .build())
    
    @staticmethod
    def create_https_token(host: str = "0.0.0.0", port: int = 20023, log_dir: str = "./logs", 
                          cert_dir: str = "./certs", key_dir: str = "./keys",
                          api_keys: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Create HTTPS configuration with token authentication."""
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.HTTPS, cert_dir=cert_dir, key_dir=key_dir)
                .set_auth(AuthMethod.TOKEN, api_keys=api_keys)
                .set_proxy_registration(enabled=False)
                .build())
    
    @staticmethod
    def create_mtls_simple(host: str = "0.0.0.0", port: int = 20024, log_dir: str = "./logs", 
                          cert_dir: str = "./certs", key_dir: str = "./keys") -> Dict[str, Any]:
        """Create simple mTLS configuration."""
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.MTLS, cert_dir=cert_dir, key_dir=key_dir)
                .set_auth(AuthMethod.NONE)
                .set_proxy_registration(enabled=False)
                .build())
    
    @staticmethod
    def create_mtls_with_roles(host: str = "0.0.0.0", port: int = 20025, log_dir: str = "./logs", 
                              cert_dir: str = "./certs", key_dir: str = "./keys",
                              roles: Optional[Dict[str, List[str]]] = None) -> Dict[str, Any]:
        """Create mTLS configuration with roles."""
        default_roles = {
            "admin": ["read", "write", "delete", "admin"],
            "user": ["read", "write"],
            "guest": ["read"]
        }
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.MTLS, cert_dir=cert_dir, key_dir=key_dir)
                .set_auth(AuthMethod.NONE, roles=roles or default_roles)
                .set_proxy_registration(enabled=False)
                .build())
    
    @staticmethod
    def create_mtls_with_proxy(host: str = "0.0.0.0", port: int = 20026, log_dir: str = "./logs", 
                              cert_dir: str = "./certs", key_dir: str = "./keys",
                              proxy_url: str = "https://127.0.0.1:20005", 
                              server_id: str = "mcp_test_server") -> Dict[str, Any]:
        """Create mTLS configuration with proxy registration."""
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.MTLS, cert_dir=cert_dir, key_dir=key_dir)
                .set_auth(AuthMethod.NONE)
                .set_proxy_registration(enabled=True, proxy_url=proxy_url, server_id=server_id, cert_dir=cert_dir)
                .build())
    
    @staticmethod
    def create_full_featured(host: str = "0.0.0.0", port: int = 20027, log_dir: str = "./logs", 
                            cert_dir: str = "./certs", key_dir: str = "./keys",
                            proxy_url: str = "https://127.0.0.1:20005", 
                            server_id: str = "mcp_full_server") -> Dict[str, Any]:
        """Create full-featured configuration with all options enabled."""
        roles = {
            "admin": ["read", "write", "delete", "admin"],
            "user": ["read", "write"],
            "guest": ["read"]
        }
        api_keys = {
            "admin": "admin-secret-key",
            "user": "user-secret-key"
        }
        return (ConfigBuilder()
                .set_server(host=host, port=port)
                .set_logging(log_dir=log_dir)
                .set_protocol(Protocol.MTLS, cert_dir=cert_dir, key_dir=key_dir)
                .set_auth(AuthMethod.TOKEN, api_keys=api_keys, roles=roles)
                .set_proxy_registration(enabled=True, proxy_url=proxy_url, server_id=server_id, cert_dir=cert_dir)
                .set_debug(enabled=True)
                .build())


def main():
    """Example usage of the configuration builder."""
    print("🔧 MCP Proxy Adapter Configuration Builder")
    print("=" * 50)
    
    # Create output directory
    output_dir = Path("configs")
    output_dir.mkdir(exist_ok=True)
    
    # Generate all standard configurations
    configs = [
        ("http_simple", ConfigFactory.create_http_simple()),
        ("http_token", ConfigFactory.create_http_token()),
        ("https_simple", ConfigFactory.create_https_simple()),
        ("https_token", ConfigFactory.create_https_token()),
        ("mtls_simple", ConfigFactory.create_mtls_simple()),
        ("mtls_with_roles", ConfigFactory.create_mtls_with_roles()),
        ("mtls_with_proxy", ConfigFactory.create_mtls_with_proxy()),
        ("full_featured", ConfigFactory.create_full_featured()),
    ]
    
    for name, config in configs:
        config_path = output_dir / f"{name}.json"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✅ Created {name}.json")
    
    print(f"\n🎉 Generated {len(configs)} configurations in {output_dir}/")


if __name__ == "__main__":
    main()
