# Function to solve the Water Jug Problem using BFS
def water_jug_problem(capacity_a, capacity_b, target):
    queue = [(0, 0)]  # Start with both jugs empty
    visited = set(queue)
    
    while queue:
        current_state = queue.pop(0)
        if current_state[0] == target or current_state[1] == target:
            return current_state
        
        # Fill jug A
        if (capacity_a, current_state[1]) not in visited:
            queue.append((capacity_a, current_state[1]))
            visited.add((capacity_a, current_state[1]))
        
        # Fill jug B
        if (current_state[0], capacity_b) not in visited:
            queue.append((current_state[0], capacity_b))
            visited.add((current_state[0], capacity_b))
        
        # Empty jug A
        if (0, current_state[1]) not in visited:
            queue.append((0, current_state[1]))
            visited.add((0, current_state[1]))
        
        # Empty jug B
        if (current_state[0], 0) not in visited:
            queue.append((current_state[0], 0))
            visited.add((current_state[0], 0))
        
        # Pour from jug A to jug B
        pour_amount = min(current_state[0], capacity_b - current_state[1])
        if (current_state[0] - pour_amount, current_state[1] + pour_amount) not in visited:
            queue.append((current_state[0] - pour_amount, current_state[1] + pour_amount))
            visited.add((current_state[0] - pour_amount, current_state[1] + pour_amount))
        
        # Pour from jug B to jug A
        pour_amount = min(current_state[1], capacity_a - current_state[0])
        if (current_state[0] + pour_amount, current_state[1] - pour_amount) not in visited:
            queue.append((current_state[0] + pour_amount, current_state[1] - pour_amount))
            visited.add((current_state[0] + pour_amount, current_state[1] - pour_amount))
    
    return None  # No solution found

# Test the program
capacity_a = 4
capacity_b = 3
target = 2
result = water_jug_problem(capacity_a, capacity_b, target)

if result:
    print("Solution found:", result)
else:
    print("No solution found.")
