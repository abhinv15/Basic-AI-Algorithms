def water_jug_problem():
    jug_a_capacity = 4  # Capacity of Jug A
    jug_b_capacity = 3  # Capacity of Jug B
    target = 2  # Target amount of water in Jug A

    # Starting with both jugs empty
    jug_a = 0
    jug_b = 0
    steps = []

    # Step-by-step solution
    steps.append((jug_a, jug_b))  # Initial state (0, 0)

    # Step 1: Fill Jug A
    jug_a = jug_a_capacity
    steps.append((jug_a, jug_b))

    # Step 2: Pour water from Jug A to Jug B until Jug B is full
    pour_amount = min(jug_a, jug_b_capacity - jug_b)
    jug_a -= pour_amount
    jug_b += pour_amount
    steps.append((jug_a, jug_b))

    # Step 3: Empty Jug B
    jug_b = 0
    steps.append((jug_a, jug_b))

    # Step 4: Pour the remaining water in Jug A into Jug B
    pour_amount = min(jug_a, jug_b_capacity - jug_b)
    jug_a -= pour_amount
    jug_b += pour_amount
    steps.append((jug_a, jug_b))

    # Step 5: Fill Jug A again
    jug_a = jug_a_capacity
    steps.append((jug_a, jug_b))

    # Step 6: Pour water from Jug A to Jug B until Jug B is full
    pour_amount = min(jug_a, jug_b_capacity - jug_b)
    jug_a -= pour_amount
    jug_b += pour_amount
    steps.append((jug_a, jug_b))

    # Print each step
    output = []
    output.append("Steps to measure exactly 2 liters:")
    for i, (a, b) in enumerate(steps):
        output.append(f"Step {i}: Jug A = {a} liters, Jug B = {b} liters")
    
    return "\n".join(output)

print(water_jug_problem())
