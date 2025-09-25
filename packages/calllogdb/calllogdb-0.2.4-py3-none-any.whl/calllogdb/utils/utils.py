from collections.abc import Mapping
from datetime import datetime, timedelta
from typing import Any


def _parse_datetime(date_str: str | None) -> datetime | None:
    """
    Преобразует строку в datetime объект, если строка соответствует формату "%Y-%m-%d %H:%M:%S".
    Возвращает None, если строка не может быть преобразована.

    Args:
        date_str (str): Строка, представляющая дату и время.

    Returns:
        (datetime | None): Преобразованный datetime объект или None, если формат неправильный.
    """
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def _parse_timedelta_seconds(value: int | str | None) -> timedelta | None:
    if not value:
        return None
    return timedelta(seconds=int(value))


def _parse_string(value: Any) -> str | None:
    if not value:
        return None
    return str(value)


def _mask_db_url(db_url: str) -> str:
    """
    Заменяет пароль в строке подключения на звёздочки.
    Предполагается, что пароль находится между ":" и "@".
    """
    import re

    return re.sub(r":([^:@]+)@", ":" + "*" * 6 + "@", db_url)


def _from_additional_info(info: dict[str, Any] | list[Any], key: str) -> str | None:
    if isinstance(info, Mapping):
        return info.get(key)
    return None
