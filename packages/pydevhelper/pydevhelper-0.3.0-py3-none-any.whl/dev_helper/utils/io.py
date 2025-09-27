import json
from typing import Any, Union, Optional

DEFAULT_ENCODING: str = "utf-8"


def write_json(
    file_path: str,
    data: Union[dict[str, Any], list[Any]],
    indent: int = 4,
    encoding: str = DEFAULT_ENCODING,
) -> None:
    with open(file_path, "w", encoding=encoding) as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def read_json(
    file_path: str,
    encoding: str = DEFAULT_ENCODING,
    safe: bool = False,
) -> Optional[Any]:
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        if safe:
            return None
        raise


def append_json_line(
    file_path: str,
    record: dict[str, Any],
    encoding: str = DEFAULT_ENCODING,
) -> None:
    with open(file_path, "a", encoding=encoding) as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def pretty_print_json(
    data: Any,
    indent: int = 4,
) -> str:
    return json.dumps(data, indent=indent, ensure_ascii=False)
