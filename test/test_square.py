"""Этот модуль проверяет правильность работы класса Square."""

import unittest

from square import Square


class TestSquareB4(unittest.TestCase):
    """Проверки поля b4."""

    def setUp(self):
        from board import Squares
        self.square = Square(Squares(), 1, 3)

    def test_file_is_correct(self):
        self.assertEqual(self.square.file, 'b')

    def test_file_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.file = 'g'
        self.assertEqual(self.square.file, 'b')

    def test_rank_is_correct(self):
        self.assertEqual(self.square.rank, '4')

    def test_rank_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.rank = '8'
        self.assertEqual(self.square.rank, '4')

    def test_file_index_is_correct(self):
        self.assertEqual(self.square.file_index, 1)

    def test_file_index_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.file_index = 3
        self.assertEqual(self.square.file_index, 1)

    def test_rank_index_is_correct(self):
        self.assertEqual(self.square.rank_index, 3)

    def test_rank_index_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.rank_index = 4
        self.assertEqual(self.square.rank_index, 3)

    def test_square_color(self):
        from color import Color
        self.assertEqual(self.square.color, Color.BLACK)

    def test_color_is_read_only(self):
        from color import Color
        with self.assertRaises(AttributeError):
            self.square.color = Color.WHITE
        self.assertEqual(self.square.color, Color.BLACK)

    def test_square_is_empty(self):
        self.assertTrue(self.square.is_empty())

    def test_square_is_on_board(self):
        self.assertTrue(self.square.is_on_board())

    def test_square_is_not_off_board(self):
        self.assertFalse(self.square.is_off_board())

    def test_square_is_not_downmost(self):
        self.assertFalse(self.square.is_downmost())

    def test_square_is_not_leftmost(self):
        self.assertFalse(self.square.is_leftmost())

    def test_square_is_not_rightmost(self):
        self.assertFalse(self.square.is_rightmost())

    def test_square_is_not_topmost(self):
        self.assertFalse(self.square.is_topmost())

    def test_down_square_is_on_board(self):
        self.assertTrue(self.square.down.is_on_board())

    def test_left_square_is_on_board(self):
        self.assertTrue(self.square.left.is_on_board())

    def test_right_square_is_on_board(self):
        self.assertTrue(self.square.right.is_on_board())

    def test_up_square_is_on_board(self):
        self.assertTrue(self.square.up.is_on_board())


class TestSquareA1(unittest.TestCase):
    """Проверки поля a1."""

    def setUp(self):
        from board import Squares
        self.square = Square(Squares(), 0, 0)

    def test_square_color(self):
        from color import Color
        self.assertEqual(self.square.color, Color.BLACK)

    def test_square_is_downmost(self):
        self.assertTrue(self.square.is_downmost())

    def test_square_is_leftmost(self):
        self.assertTrue(self.square.is_leftmost())

    def test_square_is_not_rightmost(self):
        self.assertFalse(self.square.is_rightmost())

    def test_square_is_not_topmost(self):
        self.assertFalse(self.square.is_topmost())

    def test_down_square_is_off_board(self):
        self.assertTrue(self.square.down.is_off_board())

    def test_left_square_is_off_board(self):
        self.assertTrue(self.square.left.is_off_board())

    def test_right_square_is_on_board(self):
        self.assertTrue(self.square.right.is_on_board())

    def test_up_square_is_on_board(self):
        self.assertTrue(self.square.up.is_on_board())


class TestSquareF1(unittest.TestCase):
    """Проверки поля f1."""

    def setUp(self):
        from board import Squares
        self.square = Square(Squares(), 5, 0)

    def test_square_color(self):
        from color import Color
        self.assertEqual(self.square.color, Color.WHITE)

    def test_square_is_downmost(self):
        self.assertTrue(self.square.is_downmost())

    def test_square_is_not_leftmost(self):
        self.assertFalse(self.square.is_leftmost())

    def test_square_is_not_rightmost(self):
        self.assertFalse(self.square.is_rightmost())

    def test_square_is_not_topmost(self):
        self.assertFalse(self.square.is_topmost())

    def test_down_square_is_off_board(self):
        self.assertTrue(self.square.down.is_off_board())

    def test_left_square_is_on_board(self):
        self.assertTrue(self.square.left.is_on_board())

    def test_right_square_is_on_board(self):
        self.assertTrue(self.square.right.is_on_board())

    def test_up_square_is_on_board(self):
        self.assertTrue(self.square.up.is_on_board())


class TestSquareH8(unittest.TestCase):
    """Проверки поля h8."""

    def setUp(self):
        from board import Squares
        self.square = Square(Squares(), 7, 7)

    def test_square_color(self):
        from color import Color
        self.assertEqual(self.square.color, Color.BLACK)

    def test_square_is_not_downmost(self):
        self.assertFalse(self.square.is_downmost())

    def test_square_is_not_leftmost(self):
        self.assertFalse(self.square.is_leftmost())

    def test_square_is_rightmost(self):
        self.assertTrue(self.square.is_rightmost())

    def test_square_is_topmost(self):
        self.assertTrue(self.square.is_topmost())

    def test_down_square_is_on_board(self):
        self.assertTrue(self.square.down.is_on_board())

    def test_left_square_is_on_board(self):
        self.assertTrue(self.square.left.is_on_board())

    def test_right_square_is_off_board(self):
        self.assertTrue(self.square.right.is_off_board())

    def test_up_square_is_off_board(self):
        self.assertTrue(self.square.up.is_off_board())


class TestOffBoardSquares(unittest.TestCase):
    """Проверки выхода за пределы доски."""

    def setUp(self):
        from board import Squares
        self.initial_square = Square(Squares(), 0, 0)

    def test_square_below_has_no_rank(self):
        self.assertIsNone(self.initial_square.down.rank)

    def test_square_below_has_the_same_file(self):
        self.assertEqual(self.initial_square.file, self.initial_square.down.file)

    def test_square_below_indices(self):
        self.assertEqual(self.initial_square.down.file_index, 0)
        self.assertEqual(self.initial_square.down.rank_index, -1)

    def test_square_on_the_left_has_no_file(self):
        self.assertIsNone(self.initial_square.left.file)

    def test_square_on_the_left_has_the_same_rank(self):
        self.assertEqual(self.initial_square.rank, self.initial_square.left.rank)

    def test_square_on_the_left_indices(self):
        self.assertEqual(self.initial_square.left.file_index, -1)
        self.assertEqual(self.initial_square.left.rank_index, 0)

    def test_double_left_square_has_no_file(self):
        self.assertIsNone(self.initial_square.left.left.file)

    def test_double_left_square_has_the_same_rank(self):
        self.assertEqual(self.initial_square.rank, self.initial_square.left.left.rank)

    def test_double_left_square_indices(self):
        self.assertEqual(self.initial_square.left.left.file_index, -2)
        self.assertEqual(self.initial_square.left.left.rank_index, 0)

    def test_down_left_square_has_neither_file_nor_rank(self):
        self.assertIsNone(self.initial_square.down.left.file)
        self.assertIsNone(self.initial_square.down.left.rank)

    def test_down_left_square_indices(self):
        self.assertEqual(self.initial_square.down.left.file_index, -1)
        self.assertEqual(self.initial_square.down.left.rank_index, -1)


if __name__ == '__main__':
    unittest.main()
