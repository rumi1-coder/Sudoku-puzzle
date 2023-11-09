import random
import time


# ----------------------------------------------QUESTION 1------------------------------------------------------
#
#
def generate_sudoku():
    """Generates a random 9x9 Sudoku puzzle"""
    puzzle = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            puzzle[i][j] = 0  # Clear the cell
    for i in range(1, 10):
        row = (i - 1) // 3
        col = (i - 1) % 3
        puzzle[row * 3 + col][col * 3 + row] = i  # Fill in the diagonal boxes
    for i in range(100):  # Shuffle the cells
        r1 = random.randint(0, 8)
        r2 = random.randint(0, 8)
        puzzle[r1], puzzle[r2] = puzzle[r2], puzzle[r1]  # Swap rows
        for j in range(9):
            puzzle[j][r1], puzzle[j][r2] = puzzle[j][r2], puzzle[j][r1]  # Swap columns
    for i in range(3):  # Add constraints for each 3x3 box
        for j in range(3):
            used = set([puzzle[i * 3 + k][j * 3 + l] for k in range(3) for l in range(3)])
            available = [n for n in range(1, 10) if n not in used]
            if len(available) > 0:
                row, col = random.randint(i * 3, i * 3 + 2), random.randint(j * 3, j * 3 + 2)
                while puzzle[row][col] != 0:
                    row, col = random.randint(i * 3, i * 3 + 2), random.randint(j * 3, j * 3 + 2)
                puzzle[row][col] = random.choice(available)
    return puzzle


def solve_sudoku_dfs(board):
    def dfs_helper(board, depth, num_calls):
        num_calls[0] += 1
        if depth == 81:
            return True
        # Choose the next cell with the fewest number of possible choices
        empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
        row, col = min(empty_cells, key=lambda x: len(get_choices(board, x[0], x[1])))

        for choice in get_choices(board, row, col):
            board[row][col] = choice
            if dfs_helper(board, depth + 1, num_calls):
                return True
            board[row][col] = 0
        return False

    def get_choices(board, row, col):
        choices = set(range(1, 10))
        # Remove numbers that are already in the same row, column, or 3x3 box
        choices -= set(board[row])
        choices -= set(board[i][col] for i in range(9))
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        choices -= set(board[box_row + i][box_col + j] for i in range(3) for j in range(3))
        return choices

    num_calls = [0]
    start_time = time.time()
    dfs_helper(board, sum(1 for row in board for cell in row if cell == 0), num_calls)
    end_time = time.time()
    print("Time complexity: {:.6f} seconds".format(end_time - start_time))
    print("Space complexity: {} function calls".format(num_calls[0]))


print('---------------------------')
print('GENERATING A SUDOKU PUZZLE')
print('---------------------------')
puzzle = generate_sudoku()
for row in puzzle:
    print(row)

print('')
print('---------------------------')
print('SOLVING THE ABOVE PUZZLE')
print('---------------------------')
solve_sudoku_dfs(puzzle)
for row in puzzle:
    print(row)

