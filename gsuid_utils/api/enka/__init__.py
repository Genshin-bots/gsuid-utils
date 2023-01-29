"""Enka Network 包装
参考：https://api.enka.network
"""
from .models import EnkaData as EnkaData
from .request import get_enka_info as get_enka_info

__all__ = ["request", "models"]
