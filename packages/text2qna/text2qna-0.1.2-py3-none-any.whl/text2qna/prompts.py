def build_positive_prompt(section_content: str, previous_questions: list, extra_prompt: str) -> str:
    prompt = (
        "Generate a pair of question and an answer based on the following text. "
        "The question should not be the same as previous ones and it should cover important aspects of the text "
        "that the previous haven't covered. Format the response as a question followed by its answer, for example:\n"
        "Question: add question here\n"
        "Answer: add answer here\n Your response should not contain anything else.\n"
        "Additional guidance for how to generate the question and answer: " + (extra_prompt if extra_prompt else "default") + " .\n"
    )
    if previous_questions:
        prompt += "Previous questions include: " + " ; ".join(previous_questions) + ".\n"
    return prompt + "Text: " + section_content


def build_negative_prompt(section_content: str, previous_negative_questions: list, extra_prompt: str) -> str:
    prompt = (
        "Generate a misleading or incorrect question based on the following text. "
        "Then provide a correct answer that explains the mistake. The question should be plausible but factually wrong or irrelevant. "
        "Avoid repeating previous incorrect questions. Format the response exactly as:\n"
        "Question: add incorrect or irrelevant question here\n"
        "Answer: add correct answer that explains the error\n"
        "Example:\n"
        "Question: Is Mars the closest planet to the Sun?\n"
        "Answer: No, Mars is the fourth planet from the Sun. Mercury is the closest.\n Your response should not contain anything else.\n"
        "Additional guidance for how to generate the question and answer: " + (extra_prompt if extra_prompt else "default") + " .\n"
    )
    if previous_negative_questions:
        prompt += "Previous incorrect questions include: " + " ; ".join(previous_negative_questions) + ".\n"
    return prompt + "Text: " + section_content


