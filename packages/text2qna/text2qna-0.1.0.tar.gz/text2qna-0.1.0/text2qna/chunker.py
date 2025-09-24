#!/usr/bin/env python3
"""
Helpers to convert raw documents (PDF/TXT/HTML) into semantically split Markdown.
"""

import os
import re
from typing import List, Optional

from bs4 import BeautifulSoup
import markdownify
import logging
from sklearn.metrics.pairwise import cosine_similarity
from .embeddings import EmbeddingBackend, OpenAIEmbeddings, OllamaEmbeddings, LocalEmbeddings

logger = logging.getLogger(__name__)

def _ensure_nltk_punkt_available():
    import nltk
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        try:
            nltk.download("punkt", quiet=True)
        except Exception as e:
            raise RuntimeError(
                "NLTK 'punkt' tokenizer is required for sentence splitting. "
                "Either run without --sentence-split or install the tokenizer data manually, e.g.:\n"
                "  python -c \"import nltk; nltk.download('punkt')\""
            ) from e



def load_pdf(path: str) -> str:
    # Lazy import to allow optional pdf dependency
    import pdfplumber
    text: List[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            t = re.sub(r"-\n", "", t)
            t = re.sub(r"\s+\n", "\n", t)
            text.append(t)
    return "\n\n".join(text).strip()


def load_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def load_html(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")
    return markdownify.markdownify(str(soup), heading_style="ATX")


def load_file(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf": return load_pdf(path)
    if ext in [".txt", ".text", ".md"]: return load_txt(path)
    if ext in [".html", ".htm"]: return load_html(path)
    raise ValueError(f"Unsupported input format: {ext}")


def to_markdown(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _chunk_by_words(text: str, window: int, step: int) -> List[str]:
    words = text.split()
    chunks: List[str] = []
    for i in range(0, len(words), step):
        span = " ".join(words[i:i + window]).strip()
        if span:
            chunks.append(span)
    return chunks


def _chunk_by_sentences(text: str, window: int) -> List[str]:
    _ensure_nltk_punkt_available()
    import nltk
    sentences = nltk.sent_tokenize(text)
    chunks: List[str] = []
    current: List[str] = []
    count = 0
    for sent in sentences:
        words = sent.split()
        if count + len(words) > window and current:
            chunks.append(" ".join(current))
            current, count = [], 0
        current.append(sent)
        count += len(words)
    if current:
        chunks.append(" ".join(current))
    return chunks


def semantic_split_markdown(
    md_text: str,
    embedder: EmbeddingBackend,
    sentence_split: bool = False,
    window: int = 500,
    step: int = 400,
    threshold: float = 0.70,
    min_section_words: int = 60
) -> str:
    if sentence_split:
        chunks = _chunk_by_sentences(md_text, window=window)
    else:
        chunks = _chunk_by_words(md_text, window=window, step=step)

    if not chunks:
        return md_text

    embeddings = embedder.embed(chunks)
    sections: List[str] = []
    current: List[str] = [chunks[0]]

    for i in range(1, len(chunks)):
        sim = float(cosine_similarity([embeddings[i - 1]], [embeddings[i]])[0][0])
        if sim < threshold:
            sections.append(" ".join(current).strip())
            current = [chunks[i]]
        else:
            current.append(chunks[i])
    if current:
        sections.append(" ".join(current).strip())

    merged_sections: List[str] = []
    for sec in sections:
        if merged_sections and len(sec.split()) < min_section_words:
            merged_sections[-1] += "\n\n" + sec
        else:
            merged_sections.append(sec)

    md_out_parts = [f"## Section {i+1}\n\n{sec}" for i, sec in enumerate(merged_sections)]
    return "\n\n".join(md_out_parts).strip()


