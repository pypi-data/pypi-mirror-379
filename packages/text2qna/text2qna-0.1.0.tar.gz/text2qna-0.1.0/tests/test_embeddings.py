import unittest
import numpy as np
from text2qna.embeddings import LocalEmbeddings

class TestEmbeddings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.embedder = LocalEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
        cls.test_texts = ["This is a test", "Another test text"]

    def test_embed_output_shape(self):
        embeddings = self.embedder.embed(self.test_texts)
        self.assertEqual(len(embeddings), len(self.test_texts))
        self.assertTrue(all(isinstance(emb, (list, np.ndarray)) for emb in embeddings))

        first_dim = len(embeddings[0])
        self.assertTrue(all(len(emb) == first_dim for emb in embeddings))

    def test_embed_normalized(self):
        embeddings = self.embedder.embed(self.test_texts)

        for emb in embeddings:
            norm = np.sqrt(sum(x * x for x in emb))
            self.assertAlmostEqual(norm, 1.0, places=6)

if __name__ == '__main__':
    unittest.main()