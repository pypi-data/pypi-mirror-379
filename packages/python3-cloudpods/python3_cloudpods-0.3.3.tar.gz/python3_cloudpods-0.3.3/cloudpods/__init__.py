from cloudpods.cloudpods import CloudPods
import logging
from typing import Optional

# 初始化包专属日志器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# 禁止日志向上传播（避免干扰用户项目日志器冲突）
logger.propagate = False

# 定义默认日志格式（包含时间、日志器名称、级别、消息）
DEFAULT_FORMATTER = logging.Formatter(
    fmt="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"  # 标准化时间格式
)


def _add_default_handler():
    """为日志器添加默认Handler（仅在无Handler时添加，避免重复）"""
    if not logger.handlers:
        # 添加控制台Handler（默认输出到stdout）
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(DEFAULT_FORMATTER)
        logger.addHandler(console_handler)


def get_logger(custom_formatter: Optional[logging.Formatter] = None) -> logging.Logger:
    """
    获取包的日志器，支持自定义格式

    Args:
        custom_formatter: 自定义日志格式（如不指定则使用默认格式）

    Returns:
        配置好的日志器实例
    """
    # 确保至少有一个Handler（避免"无Handler"警告）
    _add_default_handler()

    # 应用用户自定义格式（若提供）
    if custom_formatter:
        for handler in logger.handlers:
            handler.setFormatter(custom_formatter)

    return logger


__all__ = ["CloudPods", "get_logger"]

