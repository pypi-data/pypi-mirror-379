import inspect
from loguru import logger
import os
import sys
from typing import Optional, Union

LOG_COLORS = {
    "DEBUG": "\033[1;36m",  # CYAN
    "INFO": "\033[1;32m",  # GREEN
    "WARNING": "\033[1;33m",  # YELLOW
    "ERROR": "\033[1;31m",  # RED
    "CRITICAL": "\033[1;31m",  # RED
    "EXCEPTION": "\033[1;31m",  # RED
}
COLOR_RESET = "\033[1;0m"

logger.remove(0)


class Log:
    def __init__(
        self,
        filename: Optional[str] = None,
        cmdlevel: str = "DEBUG",
        filelevel: str = "INFO",
        backup_count: int = 7,  # 默认保留7天/7个文件
        limit: Union[int, str] = "20 MB",  # 支持字符串格式
        when: Optional[str] = None,
        colorful: bool = True,
        compression: Optional[str] = None,  # 新增压缩功能
        is_backtrace: bool = True,
    ):
        self.is_backtrace = is_backtrace
        self.logger = logger.bind(task=filename)
        # 设置日志文件路径
        if filename is None:
            filename = getattr(sys.modules["__main__"], "__file__", "log.py")
            filename = os.path.basename(filename.replace(".py", ".log"))

        # 确保日志目录存在
        log_dir = os.path.abspath(os.path.dirname(filename))
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 控制台输出配置
        self.logger.add(
            sys.stderr,
            level=cmdlevel,
            format=self._formatter,
            colorize=colorful,
            backtrace=True,
            enqueue=False,  # 控制台输出同步写入
            filter=lambda record: record["extra"]["task"] == filename,
        )

        # 文件输出配置
        rotation_config = self._get_rotation_config(when, limit)
        self.logger.add(
            filename,
            level=filelevel,
            format=self._formatter,
            backtrace=True,
            rotation=rotation_config,
            retention=f"{backup_count} days",
            compression=compression,
            enqueue=True,
            filter=lambda record: record["extra"]["task"] == filename,
        )

    def _formatter(self, record):
        if self.is_backtrace:
            # 获取调用栈，跳过 Loguru 和工具类的帧
            frame = inspect.currentframe()
            while frame:
                # 排除 Loguru 内部调用和工具类自身的帧
                if (
                    "loguru" not in frame.f_code.co_filename
                    and "log.py" not in frame.f_code.co_filename
                ):
                    break
                frame = frame.f_back

            # 动态获取调用函数名、文件名和行号
            func_name = frame.f_code.co_name if frame else record["function"]
            file_name = (
                os.path.basename(frame.f_code.co_filename) if frame else record["file"]
            )
            line_no = frame.f_lineno if frame else record["line"]
            file_info = f"[{file_name}:{func_name}:{line_no}] "
        else:
            file_info = f"[{record['file']}:{record['line']}]"
        level_color = LOG_COLORS.get(record["level"].name, "")
        return (
            f"{level_color}[{record['time'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] "
            + file_info
            + f"[{record['level']}] {record['message']}{COLOR_RESET}\n"
        )

    def _get_rotation_config(self, when: Optional[str], limit: Union[int, str]):
        if when:  # 时间轮转
            return when  # "D"（天）、"H"（小时）、"midnight"等
        else:  # 大小轮转
            if isinstance(limit, int):
                return f"{limit / 1024 / 1024} MB"
            return limit  # 直接支持"10 MB"、"1 GB"等字符串格式

    @staticmethod
    def set_logger(**kwargs) -> bool:
        """For backward compatibility."""
        return True

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self.logger.critical(*args, **kwargs)

    def exception(self, *args, **kwargs):
        self.logger.exception(*args, **kwargs)
