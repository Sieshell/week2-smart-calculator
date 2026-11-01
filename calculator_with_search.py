# Week 2 Project: Smart Calculator with Search

# Step 3: Basic calculation function
# Takes two numbers and an operator (+, -, *, /) and returns the result
def basic_calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Handle division by zero rather than letting it crash
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Invalid operator."


# Step 4: Brute-force search function to solve for x
# Tries every value from -100 to 100 in steps of 0.1 and keeps the closest one
def solve_for_x(expression, target):
    best_x = -100.0
    smallest_diff = float("inf")  # Start with a huge number for comparison

    # There are 2000 steps of 0.1 between -100 and 100
    current_x = -100.0
    while current_x <= 100.0:
        # Round to 1 decimal place to avoid Python floating-point weirdness (like 0.30000000004)
        x = round(current_x, 1)

        try:
            # Evaluate the math expression using the current guess for x
            result = eval(expression, {"x": x})
            diff = abs(result - target)

            # If this guess is closer to the target than our previous best, save it
            if diff < smallest_diff:
                smallest_diff = diff
                best_x = x
        except Exception:
            return None, "Error: Could not evaluate expression."

        current_x += 0.1

    return best_x, smallest_diff


# Step 3: Equation solver menu
# Asks the user for an expression with x and the target value, then prints the answer
def equation_solver_menu():
    print("\n--- Equation Solver ---")
    print("Use Python math format, for example: 2 * x + 3  or  x - 4")
    expression = input("Enter an expression containing x: ")

    if "x" not in expression:
        print("Error: Your expression must contain the variable 'x'.")
        return

    try:
        target = float(input("Enter the value it should equal: "))
    except ValueError:
        print("Error: Target must be a number.")
        return

    best_x, diff = solve_for_x(expression, target)
    if best_x is None:
        print(diff)  # Prints the error message
    else:
        print(f"Closest answer found: x = {best_x} (off by {round(diff, 4)})")


# Step 4: Search visualization
# Prints every value tried and how far it was from the target
def visualize_search():
    print("\n--- Visualizing Brute-Force Search ---")
    expression = "x + 5"
    target = 12.0
    print(f"Solving: {expression} = {target}\n")

    best_x = 0.0
    smallest_diff = float("inf")

    # Note: Narrowed the range from [-100, 100] down to [0, 10] in steps of 0.5
    # so it doesn't flood the terminal with 2,000 lines, making it easier to read.
    current_x = 0.0
    while current_x <= 10.0:
        x = round(current_x, 1)
        result = eval(expression, {"x": x})
        diff = round(abs(result - target), 2)

        print(f"Trying x = {x:4} | Result = {result:4} | Distance from target = {diff}")

        if diff < smallest_diff:
            smallest_diff = diff
            best_x = x

        current_x += 0.5

    print(f"\nSearch finished! Best value found: x = {best_x} (off by {smallest_diff})")


# Part 3 - Step 5: Interactive menu loop
def main():
    while True:
        print("\n==============================")
        print("  Smart Calculator with Search")
        print("==============================")
        print("1. Basic calculation")
        print("2. Equation solver")
        print("3. Search visualization")
        print("4. What is a search algorithm?")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ").strip()
                num2 = float(input("Enter second number: "))
                result = basic_calculate(num1, num2, operator)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "2":
            equation_solver_menu()

        elif choice == "3":
            visualize_search()

        elif choice == "4":
            print("\n--- What is a Search Algorithm? ---")
            print(
                "A brute-force search tries every single possible answer one by one "
                "until it finds the best match. It is slow because it wastes time checking "
                "thousands of bad guesses even for a simple problem. Smarter approaches, "
                "like Binary Search or A* (A-Star) Search, use rules or heuristics to "
                "skip bad options and head straight toward the goal."
            )

        elif choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
