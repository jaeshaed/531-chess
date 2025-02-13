import unittest
import unittest.mock

from square import Square


class TestSquareB4(unittest.TestCase):

    def setUp(self):
        all_squares = unittest.mock.Mock()
        self.square = Square(all_squares, 1, 3)

    def test_file_is_correct(self):
        self.assertEqual(self.square.file, 'b')

    def test_file_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.file = 'g'
        assertEqual(self.square.file, 'b')

    def test_rank_is_correct(self):
        self.assertEqual(self.square.rank, '4')

    def test_rank_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.rank = '8'
        assertEqual(self.square.rank, '4')

    def test_file_index_is_correct(self):
        self.assertEqual(self.square.file_index, 1)

    def test_file_index_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.file_index = 3
        assertEqual(self.square.file_index, 1)

    def test_rank_index_is_correct(self):
        self.assertEqual(self.square.rank_index, 3)

    def test_rank_index_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.square.rank_index = 4
        assertEqual(self.square.rank_index, 3)

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

    def setUp(self):
        all_squares = unittest.mock.Mock()
        self.square = Square(all_squares, 0, 0)

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

    def setUp(self):
        all_squares = unittest.mock.Mock()
        self.square = Square(all_squares, 5, 0)

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

    def setUp(self):
        all_squares = unittest.mock.Mock()
        self.square = Square(all_squares, 7, 7)

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


if __name__ == '__main__':
    unittest.main()
