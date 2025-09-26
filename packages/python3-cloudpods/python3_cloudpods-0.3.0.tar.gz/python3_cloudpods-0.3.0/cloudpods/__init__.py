from cloudpods.cloudpods import CloudPods
import logging
from typing import Optional


log=logging.getLogger(__name__)
log.setLevel(logging.WARNING)
log.propagate = False

def get_logger() -> logging.Logger:
    """获取包的日志器，用户可通过此函数配置日志（如添加Handler、调整级别）"""
    return log

__all__ = ["CloudPods", "get_logger"]

