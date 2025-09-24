"""text2qna — Utilities for generating Q&A fine-tuning datasets from documents.

Modules:
- qna: Generate Q&A pairs (positive/negative) from Markdown sections
- chunker: Convert raw documents into semantically split Markdown
- cli: Command-line interface entry points
"""

__version__ = "0.1.0"
__all__ = ["qna", "chunker", "__version__"]


