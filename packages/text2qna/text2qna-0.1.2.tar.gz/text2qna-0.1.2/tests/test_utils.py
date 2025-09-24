import unittest
import os
import tempfile
from text2qna.utils import read_text, write_text

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Create a temporary file
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.txt")

    def test_read_write_text(self):
        test_content = "Hello, World!"
        # Test write_text
        write_text(self.test_file, test_content)
        self.assertTrue(os.path.exists(self.test_file))
        
        # Test read_text
        read_content = read_text(self.test_file)
        self.assertEqual(test_content, read_content)

    def tearDown(self):
        # Clean up temporary files
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.test_dir)

if __name__ == '__main__':
    unittest.main()