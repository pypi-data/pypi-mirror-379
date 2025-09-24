from typing import Callable, Iterable, Dict, Any, Optional


def read_text(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def write_text(path: str, content: str, encoding: str = "utf-8") -> None:
    with open(path, "w", encoding=encoding) as f:
        f.write(content)


def write_jsonl(
    path: str,
    items: Iterable[Dict[str, Any]],
    transform: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
    encoding: str = "utf-8",
) -> None:
    import json

    with open(path, "w", encoding=encoding) as f:
        for item in items:
            payload = transform(item) if transform else item
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")


