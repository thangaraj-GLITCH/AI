def is_safe(board, row, col, N):
    # Check the current column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True
def solve_queen_util(board, row, N):
    if row == N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_queen_util(board, row + 1, N):
                return True
            board[row][col] = 0

    return False

# Function to solve the 8-Queen problem and print the solution
def solve_queen():
    N = 8
    board = [[0] * N for _ in range(N)]

    if not solve_queen_util(board, 0, N):
        print("Solution does not exist")
        return
    
    for row in board:
        print(row)

# Test the program
solve_queen()
