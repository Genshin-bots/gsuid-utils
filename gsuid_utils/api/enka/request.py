'''Enka Network 请求模块。
MiniGG Enka 加速服务在此模块内。
'''
from __future__ import annotations

from typing import Literal

from httpx import AsyncClient

from gsuid_utils.version import __version__
from gsuid_utils.api.enka.models import EnkaData

ADDRESS = {
    'enka': 'https://enka.network',
    'microgg': 'https://enka.microgg.cn',
    'minigg': 'https://enka.minigg.cn',
}


async def get_enka_info(
    uid: int, address: Literal['enka', 'microgg', 'minigg'] = 'enka'
) -> EnkaData:
    '''请求 Enka Network

    Args:
        uid (int): 原神 UID
        address (Literal[&quot;enka&quot;, &quot;microgg&quot;, &quot;minigg&quot;], optional): API 地址. Defaults to 'enka'.

    Returns:
        EnkaData: Enka Network 响应数据
    '''  # noqa: E501
    async with AsyncClient(
        base_url=ADDRESS[address],
        headers={'User-Agent': f'gsuid-utils/{__version__}'},
    ) as client:
        req = await client.get(url=f'/u/{uid}/__data.json')
        return req.json()
