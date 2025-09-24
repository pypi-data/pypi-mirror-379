from typing import TypedDict


class Section(TypedDict):
    title: str
    content: str
    level: str


class QAItem(TypedDict, total=False):
    prompt: str
    response: str
    is_negative: bool


