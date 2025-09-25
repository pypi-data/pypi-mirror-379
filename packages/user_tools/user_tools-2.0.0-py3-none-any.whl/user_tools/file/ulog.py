#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Author   : Skypekey
# @FileName : ulog
# @Time     : 2025-05-08 22:57:38

from __future__ import annotations

from datetime import time
import logging
import logging.handlers
import mimetypes
from pathlib import Path
from typing import ClassVar, TypeVar

from pydantic import ConfigDict, Field, ValidationError, field_validator
from pydantic.dataclasses import dataclass

LOG_LEVELS = logging.getLevelNamesMapping().keys()
T = TypeVar("T", bound="AppLogger")


@dataclass(config=ConfigDict(extra="forbid"))
class LogSettings:
    """日志设置模型(Pydantic v2)

    属性:
        module_name (str): 模块名称, 默认为"app"
        log_level (str): 日志级别, 必须为有效的日志级别名称, 默认为"ERROR"
        log_path (str): 日志文件存储路径, 默认为"logs"
        log_file (ClassVar[dict]): 各模块对应的日志文件名映射, 自动生成
        backup_count (int): 日志文件保留数量, 范围0-30, 默认为7

    验证规则:
        - log_level必须为有效的日志级别名称
        - backup_count必须在0-30范围内

    示例:
        >>> settings = LogSettings(module_name="my_app", log_level="INFO")
    """
    module_name: str = "app"
    log_level: str = "ERROR"
    log_path: str = "logs"
    log_file: ClassVar[dict[str, str]] = None
    backup_count: int = Field(default=7, ge=0, le=30)

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        if v not in LOG_LEVELS:
            msg = f"错误的日志级别, 只支持如下日志级别: {LOG_LEVELS}"
            raise ValueError(msg)
        return v.upper()

    def __post_init__(self) -> None:
        if self.log_file is None:
            self.log_file = {self.module_name: f"{self.module_name}.log"}


class AppLogger:
    """应用日志管理器

    提供统一的日志配置和管理功能, 支持:
    - 多模块日志记录
    - 动态配置更新
    - 错误处理和验证

    属性:
        module_name (str): 当前日志模块名称
        _logger (logging.Logger): 日志器实例
        _current_config (LogSettings): 当前日志配置

    主要方法:
        get_logger(): 获取配置好的日志器实例
        reconfigure(): 动态更新日志配置

    示例:
        # 基本用法
        logger = AppLogger("my_module").get_logger()
        logger.info("Application started")

        # 动态配置
        app_logger = AppLogger("my_module")
        app_logger.reconfigure(log_level="DEBUG")
    """

    def __init__(self, module_name: str | None = None) -> None:
        if module_name and not isinstance(module_name, str):
            msg="module_name 必须为字符串, 当前为: {}".format(
                f"{type(module_name)}")
            raise ValueError(msg)
        self.module_name = module_name.strip() or "app"
        self._initialize()

    def _initialize(self, **kwargs) -> logging.Logger:
        """初始化并配置日志系统

        该方法负责日志系统的完整配置, 包括创建日志目录、设置日志格式、
        配置处理器等。如果配置未变化且日志器已存在, 则直接返回现有日志器。

        参数:
            **kwargs: 可选的配置参数, 支持以下参数:
                - module_name (str): 模块名称
                - log_level (str): 日志级别(DEBUG/INFO/WARNING/ERROR/CRITICAL)
                - log_path (str): 日志文件存储路径
                - backup_count (int): 日志文件保留数量(0-30)

        返回:
            logging.Logger: 配置好的日志器实例

        异常:
            ValueError: 如果提供的参数无效或验证失败

        示例:
            >>> logger = AppLogger("my_module")._initialize(log_level="DEBUG")
            >>> logger.info("Debug logging enabled")
        """

        self.default_settings = LogSettings(module_name=self.module_name)

        if kwargs:
            try:
                log_settings = LogSettings(
                    module_name=self.module_name, **kwargs)
            except ValidationError as e:
                err_arg = ",".join(e.errors()[0]["loc"])
                msg = f"给定参数名称不在预定义参数列表中: {err_arg}"
                raise ValueError(msg) from e
        else:
            log_settings = self.default_settings

        if hasattr(self, "_current_config") and \
           self._current_config == log_settings and \
           self._logger is not None:
            return True

        self._current_config = log_settings

        log_path = Path(log_settings.log_path)
        log_path.mkdir(parents=True, exist_ok=True)

        self._logger = logging.getLogger(self.module_name)
        self._logger.setLevel(log_settings.log_level)

        for handler in self._logger.handlers[:]:
            self._logger.removeHandler(handler)
            handler.close()

        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(filename)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        log_file = log_settings.log_file.get(
            self.module_name, f"{self.module_name}.log")
        dst_log_file = log_path / log_file

        if dst_log_file.exists():
            mime_type, _ = mimetypes.guess_type(dst_log_file)
            if not (mime_type and mime_type.startswith("text/")):
                msg = f"日志文件存在且不为文本文件:{mime_type}"
                raise ValueError(msg)

        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=dst_log_file,
            when="midnight",
            backupCount=log_settings.backup_count,
            encoding="utf-8",
            atTime=time(0, 0, 0),
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_settings.log_level)

        self._logger.addHandler(file_handler)
        return self._logger

    def reconfigure(self, **kwargs) -> bool:
        """动态重新配置日志系统

        该方法允许在不重新创建日志器的情况下更新日志配置,
        适用于运行时调整日志级别或输出路径等场景。

        参数:
            **kwargs: 配置参数, 支持以下参数:
                - module_name (str): 模块名称
                - log_level (str): 新的日志级别
                - log_path (str): 新的日志文件存储路径
                - backup_count (int): 新的日志文件保留数量

        返回:
            bool:
                - True: 重新配置成功
                - False: 重新配置失败(保持原配置)

        异常:
            ValueError: 如果提供的参数无效或验证失败

        示例:
            >>> logger = AppLogger("my_module")
            >>> logger.reconfigure(log_level="DEBUG")  # 动态调整为DEBUG级别
            True
        """

        return self._initialize(**kwargs)


if __name__ == "__main__":
    pass
