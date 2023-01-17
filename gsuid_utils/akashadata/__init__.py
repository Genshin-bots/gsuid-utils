"""
虚空数据库 API 包装：
深渊出场数据；
"""
from .models import AkashaAbyssData as AkashaAbyssData
from .request import get_akasha_abyss_info as get_akasha_abyss_info

__all__ = ["request", "models"]
