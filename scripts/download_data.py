"""Скачивает train.csv и macro.csv соревнования Sberbank Russian Housing Market.
Оригинал лежит на Kaggle (нужна авторизация), здесь - публичное зеркало на GitHub."""
import sys
import urllib.request
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.config import RAW_DIR, RAW_URLS  # noqa: E402

RAW_DIR.mkdir(parents=True, exist_ok=True)
for name, url in RAW_URLS.items():
    dst = RAW_DIR / name
    if dst.exists():
        print(name, "уже скачан")
        continue
    print("качаю", name)
    urllib.request.urlretrieve(url, dst)
