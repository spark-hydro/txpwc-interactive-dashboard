from __future__ import annotations

from config.settings import CATALOG_PATH
from core.io.filesystem import read_json


def load_catalog() -> dict:
    return read_json(CATALOG_PATH)

def get_basin_config(basin_id: str) -> dict:
    catalog = load_catalog()
    return catalog["basins"].get(basin_id, {})