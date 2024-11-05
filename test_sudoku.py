import unittest

from sudoku import *

class TestSolveSudoku(unittest.TestCase):

    # TESTS TO WRITE:
    # is the sudoku of a valid form that is accepted by the specs?
    # can the sudoku be solved?
    # does the sudoku have a unique solution?
    # func solves the sudoku

    def setUp(self):
        self.valid_puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.solved_puzzle = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

        self.puzzle_4_by_4 = [
            [1, 2, 3, 4],
            [0, 3, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 4, 0],
        ]

    def test_valid_position(self):
        # Given a valid puzzle returns True

        puzzle = self.valid_puzzle

        self.assertTrue(is_valid_position(puzzle))


    def test_invalid_position_row(self):
        # Given a puzzle with two of the same numbers in a row, returns False

        puzzle = [# 2 fives in row 1
                [5, 3, 0, 0, 7, 0, 5, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        self.assertFalse(is_valid_position(puzzle))

    
    def test_invalid_position_col(self):
        # Given a puzzle with two of the same numbers in a column, returns False

        puzzle = [ # 2 fours in col 1
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [4, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        self.assertFalse(is_valid_position(puzzle))


    def test_invalid_position_box(self):
        # Given a puzzle with two of the same numbers in a box, returns False

        puzzle = [ # 2 sixes in box 7
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 6, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        self.assertFalse(is_valid_position(puzzle))


    def test_invert_puzzle(self):
        # Given a square puzzle returns an inverted puzzle along the top-left, bottom-right diagonal

        input_puzzle = self.valid_puzzle
        
        output_puzzle = [
                [5, 6, 0, 8, 4, 7, 0, 0, 0],
                [3, 0, 9, 0, 0, 0, 6, 0, 0],
                [0, 0, 8, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 8, 0, 0, 4, 0],
                [7, 9, 0, 6, 0, 2, 0, 1, 8],
                [0, 5, 0, 0, 3, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 2, 0, 0],
                [0, 0, 6, 0, 0, 0, 8, 0, 7],
                [0, 0, 0, 3, 1, 6, 0, 5, 9],
            ]

        self.assertEqual(invert(input_puzzle), output_puzzle)


    def test_has_no_duplicate_digits(self):
        # Given a 1d or 2d list of non-repeating sudoku digits, returns False
        
        valid_short_list = [0, 1, 2, 3]

        valid_1d_list = [0, 0, 1, 0, 2, 9, 5, 0, 0]

        valid_2d_list = self.valid_puzzle

        self.assertFalse(has_duplicates(valid_short_list))
        self.assertFalse(has_duplicates(valid_1d_list))
        self.assertFalse(has_duplicates(valid_2d_list))


    def test_has_duplicate_digits(self):
        # Given a 1d or 2d list of sudoku digits, some of which repeat, returns True
        invalid_short_list = [0, 0, 1, 1]
        invalid_1d_list = [0, 0, 3, 2, 0, 0, 9, 4, 2]
        invalid_2d_list = [ # 2 twos in row 7
            [5, 6, 0, 8, 4, 7, 0, 0, 0],
            [3, 0, 9, 0, 0, 0, 6, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 8, 0, 0, 4, 0],
            [7, 9, 0, 6, 0, 2, 0, 1, 8],
            [0, 5, 0, 0, 3, 0, 0, 9, 0],
            [2, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 6, 0, 0, 0, 8, 0, 7],
            [0, 0, 0, 3, 1, 6, 0, 5, 9],
        ]


        self.assertTrue(has_duplicates(invalid_short_list))
        self.assertTrue(has_duplicates(invalid_1d_list))
        self.assertTrue(has_duplicates(invalid_2d_list))
        

    def test_get_boxes(self):
        # Given a 9x9 puzzle returns 9 1d lists of the sudoku boxes
        
        puzzle = self.valid_puzzle
        boxes = [
            [5, 3, 0, 6, 0, 0, 0, 9, 8],
            [0, 7, 0, 1, 9, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 4, 0, 0, 7, 0, 0],
            [0, 6, 0, 8, 0, 3, 0, 2, 0],
            [0, 0, 3, 0, 0, 1, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 1, 9, 0, 8, 0],
            [2, 8, 0, 0, 0, 5, 0, 7, 9],
        ]

        self.assertEqual(get_boxes(puzzle), boxes)


    def test_get_boxes_invalid_size(self):
        # Given puzzles of too large or too small a size, raises a ValueError

        invalid_puzzle_too_small = self.puzzle_4_by_4

        invalid_puzzle_many_columns = [
            [5, 3, 0, 6, 0, 0, 0, 9, 8, 0, 0, 0],
            [0, 7, 0, 1, 9, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
            [8, 0, 0, 4, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 6, 0, 8, 0, 3, 0, 2, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 1, 0, 0, 6, 0, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 1, 9, 0, 8, 0, 0, 0, 0],
            [2, 8, 0, 0, 0, 5, 0, 7, 9, 0, 0, 0],
        ]

        invalid_puzzle_too_many_rows = [
            [5, 3, 0, 6, 0, 0, 0, 9, 8,],
            [0, 7, 0, 1, 9, 5, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 6, 0,],
            [8, 0, 0, 4, 0, 0, 7, 0, 0,],
            [0, 6, 0, 8, 0, 3, 0, 2, 0,],
            [0, 0, 3, 0, 0, 1, 0, 0, 6,],
            [0, 6, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 4, 1, 9, 0, 8, 0,],
            [2, 8, 0, 0, 0, 5, 0, 7, 9,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ]

        with self.assertRaises(ValueError):
            get_boxes(invalid_puzzle_too_small)
        with self.assertRaises(ValueError):
            get_boxes(invalid_puzzle_many_columns)
        with self.assertRaises(ValueError):
            get_boxes(invalid_puzzle_too_many_rows)


    def test_solve_sudoku(self):
        # Given a valid but not completed sudoku puzzle, tests if a completed puzzle is returned

        unsolved_puzzle = self.valid_puzzle

        solved_puzzle = self.solved_puzzle

        self.assertEqual(solve(unsolved_puzzle), solved_puzzle)


    def test_get_next_empty_coordinates(self):
        # Given a puzzle, returns the row, col coordinates for the next empty space, or None if the puzzle is complete

        unsolved_puzzle = self.valid_puzzle

        solved_puzzle = self.solved_puzzle

        self.assertTupleEqual(get_next_empty_coordinates(unsolved_puzzle), (0, 2))
        self.assertEqual(get_next_empty_coordinates(solved_puzzle), None)


    def test_is_complete_puzzle(self):
        # Given a filled out puzzle, returns True

        solved_puzzle = self.solved_puzzle

        filled_puzzle = [
            [9, 9, 9, 9, 9, 9, 9, 9, 2],
            [9, 9, 9, 9, 9, 9, 9, 9, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 7],
            [9, 9, 9, 9, 9, 9, 9, 9, 3],
            [9, 9, 9, 9, 9, 9, 9, 9, 1],
            [9, 9, 9, 9, 9, 9, 9, 9, 6],
            [9, 9, 9, 9, 9, 9, 9, 9, 4],
            [9, 9, 9, 9, 9, 9, 9, 9, 5],
            [9, 9, 9, 9, 9, 9, 9, 9, 9]
        ]

        small_puzzle = [
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [2, 4, 1, 3],
            [3, 1, 4, 2],
        ]

        big_puzzle = [
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 6],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        ]

        self.assertTrue(is_complete(solved_puzzle))
        self.assertTrue(is_complete(filled_puzzle))
        self.assertTrue(is_complete(small_puzzle))
        self.assertTrue(is_complete(big_puzzle))


    def test_is_not_complete_puzzle(self):
        # Given puzzles with unfilled spaces returns False

        unsolved_puzzle = self.valid_puzzle

        small_puzzle = self.puzzle_4_by_4

        blank_puzzle = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertFalse(is_complete(unsolved_puzzle))
        self.assertFalse(is_complete(small_puzzle))
        self.assertFalse(is_complete(blank_puzzle))


if __name__ == "__main__":
    unittest.main()