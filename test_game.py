import unittest
from unittest.mock import patch
from io import StringIO

from game import GameRole, execute_command


class TestGame(unittest.TestCase):
    def setUp(self):
        self.role = GameRole("Police")

    def test_left_move(self):
        execute_command("L", self.role)
        self.assertEqual(self.role._GameRole__x, -5)

    def test_right_move(self):
        execute_command("R", self.role)
        self.assertEqual(self.role._GameRole__x, 5)

    def test_up_move(self):
        execute_command("U", self.role)
        self.assertEqual(self.role._GameRole__y, 5)

    def test_down_move(self):
        execute_command("D", self.role)
        self.assertEqual(self.role._GameRole__y, -5)

    def test_jump_move(self):
        execute_command("JP", self.role)
        self.assertEqual(self.role._GameRole__z, 0)

    def test_squat_move(self):
        execute_command("JP", self.role)

        self.assertEqual(self.role._GameRole__z, 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_attack(self, mock_stdout):
        execute_command("A", self.role)
        self.assertEqual(mock_stdout.getvalue(), "Policelaunched an attack...\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_show_position(self, mock_stdout):
        self.role._GameRole__x = 10
        self.role._GameRole__y = -20
        self.role._GameRole__z = 30
        self.role.showPosition()
        self.assertEqual(mock_stdout.getvalue(), "Policeposition：(x:10, y:-20, z:30)\n")

    def test_left_up_move(self):
        execute_command("LU", self.role)
        self.assertEqual(self.role._GameRole__x, -5)
        self.assertEqual(self.role._GameRole__y, 5)

    def test_left_down_move(self):
        execute_command("LD", self.role)
        self.assertEqual(self.role._GameRole__x, -5)
        self.assertEqual(self.role._GameRole__y, -5)

    def test_right_up_move(self):
        execute_command("RU", self.role)
        self.assertEqual(self.role._GameRole__x, 5)
        self.assertEqual(self.role._GameRole__y, 5)

    def test_right_down_move(self):
        execute_command("RD", self.role)
        self.assertEqual(self.role._GameRole__x, 5)
        self.assertEqual(self.role._GameRole__y, -5)

    @patch("sys.stdout", new_callable=StringIO)
    def test_left_attack(self, mock_stdout):
        execute_command("LA", self.role)
        self.assertEqual(self.role._GameRole__x, -5)
        self.assertEqual(mock_stdout.getvalue(), "Policelaunched an attack...\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_attack(self, mock_stdout):
        execute_command("RA", self.role)
        self.assertEqual(self.role._GameRole__x, 5)
        self.assertEqual(mock_stdout.getvalue(), "Policelaunched an attack...\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_up_attack(self, mock_stdout):
        execute_command("UA", self.role)
        self.assertEqual(self.role._GameRole__y, 5)
        self.assertEqual(mock_stdout.getvalue(), "Policelaunched an attack...\n")
