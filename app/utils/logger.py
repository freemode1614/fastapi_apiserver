import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # 定义日志格式
    # filename="app.log",
)


def get_scoped_logger(scope: str):
    """
    Get scoped logger
    """
    return logging.getLogger(scope)
