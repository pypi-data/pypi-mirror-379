from typing import List, Optional

import numpy as np
import requests


class EmbeddingBackend:
    def embed(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError


class OpenAIEmbeddings(EmbeddingBackend):
    def __init__(self, model: str = "text-embedding-3-small", api_key: Optional[str] = None, base_url: Optional[str] = None):
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key, base_url=base_url or "https://api.openai.com/v1")
        self.model = model

    def embed(self, texts: List[str]) -> List[List[float]]:
        resp = self.client.embeddings.create(model=self.model, input=texts)
        return [d.embedding for d in resp.data]


class OllamaEmbeddings(EmbeddingBackend):
    def __init__(self, model: str = "mxbai-embed-large", base_url: str = "http://localhost:11434/api/embeddings", timeout: int = 120):
        self.model = model
        self.url = base_url.rstrip("/")
        self.timeout = timeout

    def embed(self, texts: List[str]) -> List[List[float]]:
        out: List[List[float]] = []
        for t in texts:
            r = requests.post(self.url, json={"model": self.model, "prompt": t}, timeout=self.timeout)
            r.raise_for_status()
            data = r.json()
            if "embedding" not in data:
                raise RuntimeError(f"Ollama response missing 'embedding': {data}")
            out.append(data["embedding"])
        return out


class LocalEmbeddings(EmbeddingBackend):
    def __init__(self, model: str = "sentence-transformers/all-MiniLM-L6-v2", device: Optional[str] = None):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model, device=device)

    def embed(self, texts: List[str]) -> List[List[float]]:
        vecs = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return vecs.tolist() if isinstance(vecs, np.ndarray) else list(vecs)


