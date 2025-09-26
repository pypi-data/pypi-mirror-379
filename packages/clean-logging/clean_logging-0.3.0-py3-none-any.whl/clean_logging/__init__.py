from .infrastructure.loggin_setup import setup_logging
from .core.interfaces.log_repository_interface import ILogRepository

__all__ = ["setup_logging", "ILogRepository"]