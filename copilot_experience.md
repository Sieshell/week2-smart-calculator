# GitHub Copilot Experience

## What Worked Well
* **Autocompleting repetitive menu structures:** Once I wrote a comment describing the 5-option `while True` menu loop in `main()`, Copilot quickly generated the `print` statements and `if/elif/else` branching structure, saving a lot of typing.
* **Basic arithmetic boilerplate:** In `basic_calculate()`, Copilot immediately recognized the function parameters and suggested the standard `+`, `-`, `*`, and `/` conditional checks along with a division-by-zero check (`if num2 == 0:`).
* **Input validation and error handling:** Copilot helped wrap user inputs in `try...except ValueError` blocks and added `.strip()` to string inputs so accidental spaces or non-numeric entries wouldn't crash the program.
* **Formatting print statements:** It sped up writing clean f-strings for displaying the current guess, calculated result, and distance from the target inside the search functions.

## Challenges
* **Suggesting code I did not understand:** At first, Copilot tried to suggest compact one-liners and advanced Python features (like `eval()` with dictionary comprehensions or `min()` with a `lambda` function) that were harder to read and explain step-by-step.
* **Trying to skip the brute-force loop:** Because solving linear equations is a common problem, Copilot initially wanted to solve for `x` algebraically or use external math libraries rather than stepping through every number from -100 to 100 by `0.1`.
* **Floating-point precision quirks:** When stepping by `0.1` in Python, numbers occasionally showed long decimal tails (like `0.30000000000000004`), so I had to figure out how to use `round()` properly rather than relying on Copilot's first raw loop suggestion.

## My Judgement (Where I Rejected or Changed Suggestions)
* **1. Narrowing the range in `visualize_search()`:**
  * **What Copilot suggested:** When generating `visualize_search()`, Copilot copied the exact `-100` to `100` range with a `0.1` step from `solve_for_x()`, printing every single attempt across all 2,000 iterations.
  * **What was wrong with it:** Printing 2,000 lines flooded the terminal window instantly, making it difficult to scroll back and actually see how the distance to the target shrank as `x` got closer to the answer.
  * **What I did instead:** I rejected the full `-100` to `100` range for the visualization function and narrowed the search window (with a comment explaining why) so you can clearly watch each step approach the target value without overwhelming the terminal.

* **2. Replacing complex `lambda` / `eval()` suggestions with a clear loop:**
  * **What Copilot suggested:** For `solve_for_x()`, Copilot initially suggested a condensed approach using `min()` with a `lambda` key function to find the best `x` in a single line.
  * **What was wrong with it:** While it was short, it hid the step-by-step search process, and I wanted code that clearly showed how brute-force search checks each candidate one at a time and updates the best result.
  * **What I did instead:** I wrote a straightforward loop that starts at the minimum value, increments `x` by `0.1` each step, calculates `abs(result - target)`, and explicitly updates `best_x` and `smallest_diff` whenever a closer value is found.
