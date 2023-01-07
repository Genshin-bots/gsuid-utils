import json
from pathlib import Path
from typing import Any, Generator

import pytest


@pytest.fixture(scope="module")
def enka_data() -> Generator[Any, None, None]:
    with open(Path(__file__).parent / "enka_data.json") as f:
        yield json.load(f)
