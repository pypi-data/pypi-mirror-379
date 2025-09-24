import json
import logging
from typing import List, Dict, Optional

import markdown
from bs4 import BeautifulSoup
from openai import OpenAI
from .prompts import build_positive_prompt, build_negative_prompt
from .utils import write_jsonl

logger = logging.getLogger(__name__)


def markdown_to_html(md_text: str) -> str:
    """Convert Markdown text to HTML."""
    return markdown.markdown(md_text)


def extract_sections(html_text: str) -> List[Dict[str, str]]:
    """Extract sections from HTML based on headers.

    Preserves the original script's logic for creating sections based on h1/h2/h3.
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    sections: List[Dict[str, str]] = []
    current_section: Optional[Dict[str, str]] = None

    for node in soup.find_all():
        if node.name in ['h1', 'h2', 'h3']:
            if current_section and (node.name <= current_section['level']):
                sections.append(current_section)
                current_section = {'title': node.text, 'content': '', 'level': node.name}
            elif not current_section:
                current_section = {'title': node.text, 'content': '', 'level': node.name}
        elif current_section:
            current_section['content'] += str(node)

    if current_section:
        sections.append(current_section)

    return sections


def _get_positive_prompt(section_content: str, previous_questions: List[str], extra_prompt: str) -> str:
    return build_positive_prompt(section_content, previous_questions, extra_prompt)


def _get_negative_prompt(section_content: str, previous_negative_questions: List[str], extra_prompt: str) -> str:
    return build_negative_prompt(section_content, previous_negative_questions, extra_prompt)


def _chat_once(client: OpenAI, model: str, prompt: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_qa_pairs(
    client: OpenAI,
    model: str,
    section: Dict[str, str],
    num_pairs: int,
    negative_ratio: float,
    extra_prompt: str
) -> List[Dict[str, str]]:
    """Generate positive and negative Q&A pairs for a section with retry logic.

    Mirrors the behavior of the original script, including duplicate avoidance and retries.
    """
    qas: List[Dict[str, str]] = []
    seen_questions: List[Dict[str, str]] = []  # {text, type}

    num_negatives = int(num_pairs * negative_ratio)
    num_positives = num_pairs - num_negatives

    def get_qa(prompt_type: str, max_retries: int = 3) -> Optional[Dict[str, str]]:
        retries = 0
        while retries < max_retries:
            if prompt_type == "positive":
                previous = [q['text'] for q in seen_questions if q['type'] == "positive"]
                prompt = _get_positive_prompt(section['content'], previous, extra_prompt)
            else:
                previous = [q['text'] for q in seen_questions if q['type'] == "negative"]
                prompt = _get_negative_prompt(section['content'], previous, extra_prompt)

            logger.info(f"--- Prompt to model ({prompt_type}) ---\n{prompt}")
            try:
                content = _chat_once(client, model, prompt)
                logger.info(f"Response:\n{content}")

                question, answer = content.split('\n', 1)
                question = question.replace("Question: ", "").strip()
                answer = answer.replace("Answer: ", "").strip()

                if question and answer and not any(q['text'] == question for q in seen_questions):
                    seen_questions.append({'text': question, 'type': prompt_type})
                    return {
                        'prompt': question,
                        'response': answer,
                        'is_negative': prompt_type == "negative"
                    }
                else:
                    logger.warning("Duplicate or invalid QA, retrying...")

            except Exception as e:
                logger.warning(f"Error while processing response: {e}, retrying...")

            retries += 1

        logger.warning(f"Failed to get a valid {prompt_type} QA after {max_retries} attempts.")
        return None

    # Positive QAs
    while len([q for q in qas if not q['is_negative']]) < num_positives:
        qa = get_qa("positive")
        if qa:
            qas.append(qa)

    # Negative QAs
    while len([q for q in qas if q['is_negative']]) < num_negatives:
        qa = get_qa("negative")
        if qa:
            qas.append(qa)

    return qas


def create_dataset_from_markdown(
    md_text: str,
    client: OpenAI,
    model: str,
    num_pairs_per_section: int,
    negative_ratio: float = 0.0,
    extra_prompt: str = ""
) -> List[Dict[str, str]]:
    """Create a dataset from a Markdown string with mixed QA pairs."""
    html_content = markdown_to_html(md_text)
    sections = extract_sections(html_content)
    dataset: List[Dict[str, str]] = []

    for section in sections:
        logger.info(f"=== Processing section: {section['title']} ===")
        qas = generate_qa_pairs(
            client=client,
            model=model,
            section=section,
            num_pairs=num_pairs_per_section,
            negative_ratio=negative_ratio,
            extra_prompt=extra_prompt,
        )
        dataset.extend(qas)

    return dataset


def save_dataset_jsonl(items: List[Dict[str, str]], output_path: str) -> None:
    """Save dataset to JSONL, excluding internal fields like 'is_negative'."""
    write_jsonl(output_path, items, transform=lambda it: {k: v for k, v in it.items() if k != 'is_negative'})


