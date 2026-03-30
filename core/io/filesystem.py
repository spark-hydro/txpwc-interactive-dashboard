from __future__ import annotations

from pathlib import Path
import json
import pandas as pd


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_csv(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)


def safe_markdown_read(path: Path) -> str:
    if not path.exists():
        return f"Missing markdown content: `{path}`"
    return path.read_text(encoding="utf-8")
