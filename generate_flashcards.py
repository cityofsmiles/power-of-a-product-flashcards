import sympy as sp
import random
import json

# Variables to use
variables = [sp.symbols(v) for v in ["x", "y", "z", "a", "b"]]

# Integer ranges
coeff_range = list(range(-5, 6))  # coefficients from -5 to 5
exp_range = list(range(-3, 4))    # exponents from -3 to 3

flashcards = []

def format_expr(expr):
    """Format Sympy expression into plain text with ^ for exponents, no *."""
    s = sp.sstr(expr)  # Sympy string
    s = s.replace("**", "^")  # Python power -> ^
    s = s.replace("*", "")    # Remove multiplication signs
    return s

def generate_flashcard():
    c = random.choice([i for i in coeff_range if i != 0])  # nonzero coefficient
    v1, v2 = random.sample(variables, 2)
    m = random.choice(exp_range)
    n = random.choice(exp_range)
    p = random.choice(exp_range)

    # Expression
    expr = (c * v1**m * v2**n)**p

    # Simplify with Sympy
    simplified = sp.simplify(expr)

    # Question in plain text
    question = f"({c}{v1}^{m}{v2}^{n})^{p}"

    return {
        "question": question,
        "answer": format_expr(simplified)   # clean plain-text answer
    }

# Generate 120 flashcards
for _ in range(120):
    flashcards.append(generate_flashcard())

# Save to JSON
with open("flashcards.json", "w") as f:
    json.dump(flashcards, f, indent=2)

print("✅ flashcards.json generated with", len(flashcards), "flashcards.")