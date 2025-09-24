import argparse
import os
import sys

from typing import Optional

from openai import OpenAI

from .qna import create_dataset_from_markdown, save_dataset_jsonl
from .chunker import (
    load_file,
    to_markdown,
    semantic_split_markdown,
)
from .embeddings import OpenAIEmbeddings, OllamaEmbeddings, LocalEmbeddings
from .config import from_env
import logging


def _build_client(api_key: Optional[str], base_url: Optional[str]) -> OpenAI:
    return OpenAI(api_key=api_key, base_url=base_url)


def _cmd_qna(args: argparse.Namespace) -> int:
    _configure_logging(args)
    env = from_env()
    client = _build_client(api_key=args.api_key or env.api_key, base_url=args.base_url or env.base_url)
    model = args.model or env.chat_model

    with open(args.input, 'r', encoding='utf-8') as f:
        md_text = f.read()

    dataset = create_dataset_from_markdown(
        md_text=md_text,
        client=client,
        model=model,
        num_pairs_per_section=args.num_pairs,
        negative_ratio=args.negative_ratio,
        extra_prompt=args.extra_prompt or "",
    )

    out = args.output or "dataset.jsonl"
    save_dataset_jsonl(dataset, out)
    print(f"✅ Dataset written to: {out}")
    return 0


def _get_embedder(args: argparse.Namespace):
    env = from_env()
    backend = args.backend or env.embed_backend
    # Resolve model per backend
    resolved_model = args.embed_model or env.embed_model
    if backend == "openai":
        resolved_model = resolved_model or "text-embedding-3-small"
        embedder = OpenAIEmbeddings(model=resolved_model, api_key=args.api_key or env.api_key, base_url=args.base_url or env.base_url)
    elif backend == "ollama":
        resolved_model = resolved_model or "mxbai-embed-large"
        embedder = OllamaEmbeddings(model=resolved_model, base_url=args.embeddings_url or env.embeddings_url or "http://localhost:11434/api/embeddings")
    else:
        backend = "local"
        resolved_model = resolved_model or "sentence-transformers/all-MiniLM-L6-v2"
        embedder = LocalEmbeddings(model=resolved_model, device=args.device or env.device)

    return embedder, backend, resolved_model


def _cmd_chunk(args: argparse.Namespace) -> int:
    _configure_logging(args)
    raw_text = load_file(args.input)
    md_text = to_markdown(raw_text)
    embedder, resolved_backend, resolved_model = _get_embedder(args)

    md_split = semantic_split_markdown(
        md_text,
        embedder=embedder,
        sentence_split=args.sentence_split,
        window=args.window,
        step=args.step,
        threshold=args.threshold,
    )

    out_path = args.output or os.path.splitext(args.input)[0] + ".md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_split)

    print(f"✅ Markdown saved to: {out_path}")
    print(f"🔎 Backend: {resolved_backend}:{resolved_model}")
    print(f"⚙️  window={args.window}, step={args.step}, threshold={args.threshold}, sentence_split={args.sentence_split}")
    return 0


def _configure_logging(args: argparse.Namespace) -> None:
    level = logging.INFO
    if getattr(args, "quiet", False):
        level = logging.WARNING
    if getattr(args, "verbose", False):
        level = logging.DEBUG
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="text2qna", description="Q&A dataset and document chunking CLI")
    sub = p.add_subparsers(dest="cmd", required=True)
    for parser in (p,):
        parser.add_argument("--quiet", action="store_true", help="Reduce log verbosity")
        parser.add_argument("--verbose", action="store_true", help="Increase log verbosity")

    # qna subcommand
    pq = sub.add_parser("qna", help="Generate Q&A dataset from Markdown file")
    pq.add_argument("input", help="Input Markdown file path")
    pq.add_argument("--model", help="Chat model name (default from env TEXT2QNA_MODEL or 'llama3.2')")
    pq.add_argument("--num-pairs", type=int, default=3, help="Pairs per section")
    pq.add_argument("--negative-ratio", type=float, default=0.0, help="Fraction of negative QAs per section")
    pq.add_argument("--extra-prompt", default="", help="Additional guidance for Q&A generation")
    pq.add_argument("--output", help="Output JSONL file (default: dataset.jsonl)")
    pq.add_argument("--api-key", help="API key for any OpenAI-compatible API (default: TEXT2QNA_API_KEY environment variable)")
    pq.add_argument("--base-url", help="Base URL for OpenAI-compatible API endpoint (default: TEXT2QNA_BASE_URL environment variable)")
    pq.set_defaults(func=_cmd_qna)

    # chunk subcommand
    pc = sub.add_parser("chunk", help="Convert documents to semantically split Markdown")
    pc.add_argument("input", help="Input file path (.pdf, .txt, .html, .md)")
    pc.add_argument("--backend", choices=["openai", "ollama", "local"], help="Embedding backend (default from env TEXT2QNA_EMBED_BACKEND or 'local')")
    pc.add_argument("--embed-model", help="Embedding model name for backend")
    pc.add_argument("--embeddings-url", help="Custom URL for Ollama embeddings endpoint")
    pc.add_argument("--output", help="Output Markdown file (default: <input>.md)")
    pc.add_argument("--threshold", type=float, default=0.70)
    pc.add_argument("--window", type=int, default=500)
    pc.add_argument("--step", type=int, default=400)
    pc.add_argument("--sentence-split", type=lambda x: str(x).lower() in ["true", "1", "yes"], default=False,
                    help="Use sentence-based splitting (default: false)")
    pc.add_argument("--api-key", help="API key for OpenAI-compatible embeddings (default: TEXT2QNA_API_KEY environment variable)")
    pc.add_argument("--base-url", help="Base URL for OpenAI-compatible API endpoint (default: TEXT2QNA_BASE_URL environment variable)")
    pc.add_argument("--device", help="Device for local embeddings (cpu, cuda, mps)")
    pc.set_defaults(func=_cmd_chunk)

    return p


def main(argv: Optional[list] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())


