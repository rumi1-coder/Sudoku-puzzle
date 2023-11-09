 #----------------------------------------------QUESTION 2------------------------------------------------------

def generate_magic_square():
      #Create an empty 3x3 matrix
     puzzle = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

      #Generate a random permutation of the numbers 1 through 9
     nums = random.sample(range(1, 10), 9)

     # Place the numbers in the cells of the puzzle
     idx = 0
     for i in range(3):
         for j in range(3):
             puzzle[i][j] = nums[idx]
             idx += 1

     return puzzle


def solve_magic_square(puzzle):
    start_state = (tuple(map(tuple, puzzle)), find_blank(puzzle), 0)
    visited = set()
    stack = [start_state]

    while stack:
        state, blank_idx, num_moves = stack.pop()
        if state in visited:
            continue
        visited.add(state)

        if is_magic_square(state):
            return state, num_moves

        for move in possible_moves(blank_idx):
            new_state = [list(row) for row in state]
            new_state[blank_idx // 3][blank_idx % 3], new_state[move // 3][move % 3] = new_state[move // 3][move % 3], new_state[blank_idx // 3][blank_idx % 3]
            new_state = tuple(map(tuple, new_state))
            if new_state not in visited:
                stack.append((new_state, move, num_moves + 1))

    return None








def find_blank(puzzle):
     for i in range(3):
         for j in range(3):
             if puzzle[i][j] == 9:
                 return i * 3 + j


def is_magic_square(puzzle):
     puzzle = [list(row) for row in puzzle]
     magic_sum = 15
     rows = puzzle
     cols = [[puzzle[j][i] for j in range(3)] for i in range(3)]
     diags = [[puzzle[i][i] for i in range(3)], [puzzle[i][2-i] for i in range(3)]]

     for group in rows + cols + diags:
         if sum(group) != magic_sum:
             return False

     return True





def possible_moves(blank_idx):
     moves = []
     if blank_idx // 3 > 0:
         moves.append(blank_idx - 3)
     if blank_idx // 3 < 2:
         moves.append(blank_idx + 3)
     if blank_idx % 3 > 0:
         moves.append(blank_idx - 1)
     if blank_idx % 3 < 2:
         moves.append(blank_idx + 1)
     return moves


start_time = time.time()

puzzle = generate_magic_square()

for row in puzzle:
    print(row)

print('')
print('---------------------------')
print('SOLVING THIS MAGIC SQUARE')
print('---------------------------')

start_time_solve = time.time()

solution, num_moves = solve_magic_square(puzzle)

if solution:
     for row in solution:
         print(row)
     print(f'Solved in {num_moves} moves.')
else:
     print('No')

end_time_solve = time.time()

print('')
print('---------------------------')
print('STATISTICS')
print('---------------------------')

print(f'Time taken to solve the puzzle: {end_time_solve - start_time_solve:.5f} seconds')
