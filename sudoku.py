# CORE BEHAVIOURS
import copy

def is_valid_position(puzzle):
    """A valid sudoku must have no duplicate digits in rows, columns or digits."""
    
    rows_have_duplicates = has_duplicates(puzzle)
    if rows_have_duplicates:
        return False
    
    columns_have_duplicates = has_duplicates(invert(puzzle))
    if columns_have_duplicates:
        return False

    boxes_have_duplicates = has_duplicates(get_boxes(puzzle))
    if boxes_have_duplicates:
        return False

    return True


def solve(puzzle):
    """This is a brute force solution - checking the validity of every digit in every cell. It is slow!"""

    # Base case - puzzle is complete (and correct)
    if is_complete(puzzle):
        return puzzle
    
    # Recursive case - puzzle is incomplete and correct
        
    # Make the next guess.
    # A deep copy of the puzzle is made for each guess. The original is needed to revert to when later guesses are wrong.
    x, y = get_next_empty_coordinates(puzzle)
    next_guess_puzzle = copy.deepcopy(puzzle)

    # Try every digit
    for digit in range(1, 10):
        next_guess_puzzle[x][y] = digit

        # Make sure the new guess is valid
        if is_valid_position(next_guess_puzzle):
            
            # Recursive case - solve the puzzle based on the latest valid guess
            solution = solve(next_guess_puzzle)
            if solution:
                return solution
    
    # All digits have been tried for the next available cell and none are valid, unwinding the recursion.
    return False



# HELPER FUNCTIONS


def get_next_empty_coordinates(puzzle):
    """Returns a tuple of (x, y) for the coordinates of the next empty (with a 0) cell. If the puzzle is complete,
    returns None."""

    for x, row in enumerate(puzzle):
        for y, cell in enumerate(row):
            if cell == 0:
                return (x, y)
    
    return None


def is_complete(puzzle):
    """Returns a boolean to indicate whether a puzzle is completely filled, but no checking is done as to correctness."""
    
    next_empty = get_next_empty_coordinates(puzzle)

    if next_empty:
        return False
    
    return True    


def invert(puzzle):
    """Returns a copy of the puzzle, inverted along the the top left to bottom right (negative) diagonal.
    Effectively this turns rows to columns and vice versa and is helpful for getting the columns in a 2D array puzzle."""

    # E.g.      ij
    # a b c     00, 01, 02
    # d e f     10, 11, 12
    # g h i     20, 21, 22
    # ---->
    # a d g
    # b e h
    # c f i

    inverted_puzzle = copy.deepcopy(puzzle)

    for x, row in enumerate(inverted_puzzle):
        for y, col in enumerate(row):
            
            # Cells down the negative diagonal (where x == y) stay where they are, and only one swap is necessary per
            # pair of digits, so, arbitrarily, this function swaps when the column is larger than the row index.
            if x > y:
                # swap the cells
                temp = inverted_puzzle[x][y]
                inverted_puzzle[x][y] = inverted_puzzle[y][x]
                inverted_puzzle[y][x] = temp

    return inverted_puzzle


def has_duplicates(lst):
    """Determines whether a 1d or multidimensional list has any duplicates. In the case of multidimensional lists,
    duplicates are within sub-lists, not the whole array."""
    
    # Collector for determining what digits have already been seen
    digit_count = {}

    for item in lst:

        # Call the function recursively if lst is a multidimensional list
        if type(item) == list:
            item_has_duplicates = has_duplicates(item)
            if item_has_duplicates:
                return True
            
        # Otherwise test the digits
        else:
            if item in digit_count:
                return True
            if item != 0:
                digit_count[item] = 1

    return False


def get_boxes(puzzle):
    """Returns a list of the boxes in a standard 9x9 sudoku. Each box is a 1d list of digits from the top left to the 
    bottom right read left to right top to bottom."""

    # Validate the puzzle as a 9x9 grid

    if len(puzzle) != 9:
        raise ValueError("The puzzle must have 9 rows for get_boxes to return boxes.")
    
    for row in puzzle:
        if len(row) != 9:
            raise ValueError("The puzzle must have 9 columns for get_boxes to return boxes.")
    

    # Build each box

    boxes = []

    for box_index in range(9):
        
        box = []

        starting_row = (box_index // 3) * 3
        starting_col = (box_index % 3) * 3

        for cell in range(9):
            row = starting_row + cell // 3
            col = starting_col + cell % 3
            box.append(puzzle[row][col])

        boxes.append(box)

    return boxes