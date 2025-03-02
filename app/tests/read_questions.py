import unittest
import json
from app.api.api import read_questions  # Adjust the import path accordingly

class TestReadQuestions(unittest.TestCase):
    def test_question_found_at_valid_position(self):
        with open('data/questions.json', 'w') as f:
            json.dump([{'position': 1, 'question': 'What is your name?'}], f)
        self.assertEqual(read_questions(1)['question'], 'What is your name?')

    def test_question_not_found_at_invalid_position(self):
        with open('data/questions.json', 'w') as f:
            json.dump([{'position': 1, 'question': 'What is your name?'}], f)
        self.assertIsNone(read_questions(2))

    def test_question_not_found_at_non_existent_position(self):
        with open('data/questions.json', 'w') as f:
            json.dump([], f)
        self.assertIsNone(read_questions(1))

    def test_error_handling_for_non_integer_position(self):
        with self.assertRaises(TypeError):
            read_questions('a')

    def test_error_handling_for_file_not_found(self):
        import os
        os.remove('data/questions.json')  # remove the file if it exists
        with self.assertRaises(FileNotFoundError):
            read_questions(1)

if __name__ == '__main__':
    unittest.main()