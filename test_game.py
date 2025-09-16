import unittest
from unittest.mock import patch
from io import StringIO
import sys

from Word_based_dungeon_adventure import stairs, square, mirror, story

class TestDungeonGame(unittest.TestCase):

    def test_stairs(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            stairs(3)
            output = fake_out.getvalue().strip().splitlines()
        self.assertIn("▥▥▥", output)

    def test_square(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square(3)
            output = fake_out.getvalue().strip().splitlines()
        self.assertEqual(len(output), 3)

    def test_mirror(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            mirror("abc")
            output = fake_out.getvalue().strip()
        self.assertEqual(output, "cba")

    @patch('builtins.input', side_effect=["y"])
    def test_story_stairs(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            story(1)
            output = fake_out.getvalue()
        self.assertIn("stairs", output.lower())

if __name__ == "__main__":
    unittest.main()
