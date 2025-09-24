#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PyQt5 统一出口（为上层项目提供稳定导入路径）"""

# 仅提供命名空间引用，避免顶层 import 开销  #
import PyQt5 as _PyQt5  # noqa: F401 #

from PyQt5 import QtCore, QtGui, QtWidgets  # 常用子模块 #

__all__ = [
    "QtCore",
    "QtGui",
    "QtWidgets",
]


