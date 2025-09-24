from typing import List, Dict, Optional


class RetryPolicy:
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries


class DuplicateFilter:
    def __init__(self):
        self._seen: List[Dict[str, str]] = []

    def add_if_new(self, question_text: str, qtype: str) -> bool:
        if any(q['text'] == question_text for q in self._seen):
            return False
        self._seen.append({'text': question_text, 'type': qtype})
        return True

    def previous_of_type(self, qtype: str) -> List[str]:
        return [q['text'] for q in self._seen if q['type'] == qtype]


