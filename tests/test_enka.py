import pytest


@pytest.mark.asyncio
async def test_enka(enka_data):
    from gsuid_utils.enka import get_enka_info

    data = await get_enka_info(821819570)
    data.pop("ttl")  # type: ignore
    assert data == enka_data


@pytest.mark.asyncio
async def test_mirror(enka_data):
    from gsuid_utils.enka import get_enka_info

    data = await get_enka_info(821819570, "microgg")
    data.pop("ttl")  # type: ignore
    assert data == enka_data

    data = await get_enka_info(821819570, "minigg")
    data.pop("ttl")  # type: ignore
    assert data == enka_data
