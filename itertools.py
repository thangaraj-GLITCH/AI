import itertools

# Function to solve the Cryptarithmetic problem
def solve_cryptarithmetic(puzzle):
    # Extracting unique letters from the puzzle
    unique_letters = set(char for char in puzzle if char.isalpha())
    
    # Generate all possible permutations of digits for unique letters
    for perm in itertools.permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        equation = puzzle.translate(str.maketrans(mapping))
        if eval(equation):
            return mapping
    return None

# Test the program
puzzle = "SEND + MORE = MONEY"
solution = solve_cryptarithmetic(puzzle)

if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
