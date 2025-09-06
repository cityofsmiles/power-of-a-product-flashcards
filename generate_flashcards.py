import sympy as sp
import random
import json

# Variables to use
variables = [sp.symbols(v) for v in ["x", "y", "z", "a", "b"]]

# Integer ranges
coeff_range = list(range(-5, 6))  # avoid 0 later
exp_range = list(range(-3, 4))    # -3 to 3

flashcards = []

def generate_flashcard():
    c = random.choice([i for i in coeff_range if i != 0])  # nonzero coefficient
    v1, v2 = random.sample(variables, 2)
    m = random.choice(exp_range)
    n = random.choice(exp_range)
    p = random.choice(exp_range)

    expr = (c * v1**m * v2**n)**p

    # Simplify with sympy
    simplified = sp.simplify(expr)

    # Handle pretty printing
    question = f"({c}{v1}^{m}{v2}^{n})^{p}"
    answer = sp.pretty(simplified)

    return {
        "question": question,
        "answer": str(simplified),   # plain string for frontend checking
        "pretty_answer": answer      # nice display for UI
    }

# Generate 120 flashcards (40 per case approx.)
for _ in range(120):
    flashcards.append(generate_flashcard())

# Save to JSON
with open("flashcards.json", "w") as f:
    json.dump(flashcards, f, indent=2)

print("✅ flashcards.json generated with", len(flashcards), "flashcards.")