import unittest
from text2qna.prompts import build_positive_prompt, build_negative_prompt

class TestPrompts(unittest.TestCase):
    def setUp(self):
        self.sample_text = "This is a sample text for testing."
        self.previous_questions = ["What is the first question?", "What is the second question?"]
        self.extra_prompt = "Keep it simple"

    def test_build_positive_prompt(self):
        prompt = build_positive_prompt(self.sample_text, self.previous_questions, self.extra_prompt)

        self.assertIn(self.sample_text, prompt)
        self.assertIn(self.extra_prompt, prompt)
        for q in self.previous_questions:
            self.assertIn(q, prompt)

    def test_build_negative_prompt(self):
        prompt = build_negative_prompt(self.sample_text, self.previous_questions, self.extra_prompt)

        self.assertIn(self.sample_text, prompt)
        self.assertIn(self.extra_prompt, prompt)
        for q in self.previous_questions:
            self.assertIn(q, prompt)

if __name__ == '__main__':
    unittest.main()