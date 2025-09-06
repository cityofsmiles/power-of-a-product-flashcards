# Power of a Product Flashcards

An interactive flashcard web app for practicing the **Power of a Product Rule of Exponents**.  
Frontend built with **React** + **TailwindCSS** + **Framer Motion**, backend flashcard generation powered by **Python + Sympy**.

👉 Live Demo: [https://cityofsmiles.github.io/power-of-a-product-flashcards](https://cityofsmiles.github.io/power-of-a-product-flashcards)

---

## 📘 Overview

This project demonstrates a **hybrid workflow**:

- **Python (backend logic)**  
  - Generates all math expressions using **Sympy**.  
  - Simplifies answers using the rules of exponents.  
  - Exports the data to a single JSON file (`flashcards.json`).  

- **React (frontend UI)**  
  - Reads `flashcards.json` locally.  
  - Displays flashcards with animations, answer checking, and scoring.  
  - Provides a smooth UX for practice and review.  

---

## 🧮 Math Coverage

The flashcards are based on the **Power of a Product Rule**:

\[
(cx^m y^n)^p = c^p x^{mp} y^{np}
\]

where  
- \(c\) is a nonzero integer,  
- \(m, n, p, q\) are integers in \([-3, 3]\),  
- \(x, y, z, a, b\) are variables.

### Cases Included
1. **Positive exponents**  
   Example: \((2x^3y^2)^3 = 8x^9y^6\)

2. **Negative exponents** (simplified with negative exponent rule)  
   Example: \((2x^{-3}y^2)^3 = \frac{8y^6}{x^9}\)

3. **Zero exponents** (simplified with zero exponent rule)  
   Example: \((-8a^3b^{-2})^0 = 1\)

---

## ⚙️ How It Works

### 1. Generate Flashcards (Python)
Run the generator script to produce `flashcards.json`:

```bash
python generate_flashcards.py