import sympy as sp
import random
import json
import os

# Variables to use
variables = [sp.symbols(v) for v in ["x", "y", "z", "a", "b"]]

# Integer ranges
coeff_range = list(range(-5, 6))  # coefficients -5 to 5, excluding 0
exp_range = list(range(-3, 4))    # inside exponents
outside_exp_range = [i for i in range(-3, 4) if i != 1]  # outside exponent, skip 1

flashcards = []

def format_expr(expr):
    """Format Sympy expression into plain text with ^ for exponents, no *."""
    s = sp.sstr(expr)
    s = s.replace("**", "^")
    s = s.replace("*", "")
    s = s.replace("^1", "")
    return s

def format_question(c, v1, m, v2, n, p):
    """Build question string with proper coefficient rules."""
    # Numerical coefficient formatting
    if c == 1:
        part1 = ""   # omit 1
    elif c == -1:
        part1 = "-"  # show minus only
    else:
        part1 = f"{c}"

    # Variables
    part2 = f"{v1}^{m}" if m != 1 else f"{v1}" if m != 0 else ""
    part3 = f"{v2}^{n}" if n != 1 else f"{v2}" if n != 0 else ""

    base = part1 + part2 + part3

    # Outside exponent, skip 1 (we never allow p=1 anyway)
    return f"({base})^{p}" if p != 1 else f"({base})"

def generate_flashcard():
    c = random.choice([i for i in coeff_range if i != 0])
    v1, v2 = random.sample(variables, 2)
    m = random.choice(exp_range)
    n = random.choice(exp_range)
    p = random.choice(outside_exp_range)  # outside exponent

    expr = (c * v1**m * v2**n)**p
    simplified = sp.simplify(expr)

    question = format_question(c, v1, m, v2, n, p)

    return {
        "question": question,
        "answer": format_expr(simplified)
    }

# Generate 120 flashcards
flashcards = [generate_flashcard() for _ in range(120)]

# Save to public folder
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "flashcards.json")

with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")