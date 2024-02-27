from itertools import permutations

def solve(puzzle):
    words = puzzle.split()
    uc = set(''.join(words))
    if len(uc) > 10:
        return "Invalid input: More than 10 unique characters"

    chars = ''.join(uc)
    for perm in permutations('1234567890', len(uc)):
        m = dict(zip(chars, perm))
        if all(int(''.join(m[c] for c in word)) != 0 for word in words):
            if sum(int(''.join(m[c] for c in word)) for word in words[:-1]) == int(''.join(m[c] for c in words[-1])):
                return {k: int(v) for k, v in m.items()}

    return "No solution found"
puzzle = "SIX SIX FIVE"
solution = solve(puzzle)
print(solution)
