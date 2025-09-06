import sympy as sp
import random
import json
import os

# Variables to use
variables = [sp.symbols(v) for v in ["x", "y", "z", "a", "b"]]

# Integer ranges
coeff_range = list(range(-5, 6))  # coefficients from -5 to 5
exp_range = list(range(-3, 4))    # exponents from -3 to 3

flashcards = []

def format_expr(expr):
    """Format Sympy expression into plain text with ^ for exponents, no *."""
    s = sp.sstr(expr)
    s = s.replace("**", "^")   # Python power -> ^
    s = s.replace("*", "")     # Remove multiplication signs
    s = s.replace("^1", "")    # Remove ^1
    return s

def format_question(c, v1, m, v2, n, p):
    """Build a clean question string with coefficient rules."""
    # Handle coefficient formatting
    if c == -1:
        part1 = "-"  # just a minus sign
    else:
        part1 = f"{c}"

    # Handle variable exponents
    part2 = f"{v1}^{m}" if m != 1 else f"{v1}" if m != 0 else ""
    part3 = f"{v2}^{n}" if n != 1 else f"{v2}" if n != 0 else ""

    base = part1 + part2 + part3
    return f"({base})^{p}"

def generate_flashcard():
    while True:
        c = random.choice([i for i in coeff_range if i != 0])  # nonzero coefficient
        v1, v2 = random.sample(variables, 2)
        m = random.choice(exp_range)
        n = random.choice(exp_range)
        p = random.choice(exp_range)

        # Skip boring outside exponent = 1
        if p == 1:
            continue

        expr = (c * v1**m * v2**n)**p
        simplified = sp.simplify(expr)

        question = format_question(c, v1, m, v2, n, p)

        return {
            "question": question,
            "answer": format_expr(simplified)
        }

# Generate 120 flashcards
for _ in range(120):
    flashcards.append(generate_flashcard())

# Ensure public folder exists
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)

# Save to public/flashcards.json
output_path = os.path.join(output_dir, "flashcards.json")
with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")