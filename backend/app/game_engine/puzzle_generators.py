import random
from typing import Dict, Any, List


class ProceduralPuzzleGenerator:
    """
    Generates dynamic procedural math, bitwise logic, and code comprehension puzzles
    on the fly for unlimited quick challenge variation.
    """

    @classmethod
    def generate_arithmetic_sequence_puzzle(cls, difficulty: str = "MEDIUM") -> Dict[str, Any]:
        """Generate a mathematical polynomial sequence puzzle."""
        if difficulty == "EASY":
            start = random.randint(1, 10)
            step = random.randint(2, 7)
            seq = [start + i * step for i in range(5)]
            next_val = start + 5 * step
            explanation = f"Arithmetic progression with common difference +{step}."
        elif difficulty == "MEDIUM":
            start = random.randint(2, 5)
            ratio = random.randint(2, 3)
            seq = [start * (ratio ** i) for i in range(4)]
            next_val = start * (ratio ** 4)
            explanation = f"Geometric progression with common ratio *{ratio}."
        else:
            # Quadratic sequence: a*n^2 + b*n + c
            a = random.randint(1, 2)
            b = random.randint(1, 3)
            seq = [a * (n ** 2) + b * n for n in range(1, 6)]
            next_val = a * (6 ** 2) + b * 6
            explanation = f"Second-order polynomial sequence: an^2 + bn."

        seq_str = ", ".join(str(x) for x in seq)
        question = f"What is the next number in the sequence: {seq_str}, __?"

        wrong_options = set()
        while len(wrong_options) < 3:
            offset = random.choice([-3, -2, -1, 1, 2, 3, 5, 10, -5])
            cand = next_val + offset
            if cand != next_val and cand > 0:
                wrong_options.add(cand)

        answers = [{"text": str(next_val), "is_correct": True}] + [
            {"text": str(w), "is_correct": False} for w in wrong_options
        ]
        random.shuffle(answers)

        return {
            "title": f"{difficulty.capitalize()} Number Sequence Pattern",
            "question": question,
            "difficulty": difficulty,
            "points": 15 if difficulty == "EASY" else (25 if difficulty == "MEDIUM" else 40),
            "time_limit_seconds": 20,
            "explanation": explanation,
            "tags": "mathematics,sequences,procedural",
            "answers": answers
        }

    @classmethod
    def generate_bitwise_puzzle(cls, difficulty: str = "MEDIUM") -> Dict[str, Any]:
        """Generate a bitwise operator evaluation challenge."""
        a = random.randint(3, 15)
        b = random.randint(2, 8)
        op_type = random.choice(["AND", "OR", "XOR", "SHIFT_LEFT"])

        if op_type == "AND":
            res = a & b
            expr = f"{a} & {b}"
            expl = f"Bitwise AND of {bin(a)} & {bin(b)} = {bin(res)} ({res})."
        elif op_type == "OR":
            res = a | b
            expr = f"{a} | {b}"
            expl = f"Bitwise OR of {bin(a)} | {bin(b)} = {bin(res)} ({res})."
        elif op_type == "XOR":
            res = a ^ b
            expr = f"{a} ^ {b}"
            expl = f"Bitwise XOR of {bin(a)} ^ {bin(b)} = {bin(res)} ({res})."
        else:
            shift = random.randint(1, 3)
            res = a << shift
            expr = f"{a} << {shift}"
            expl = f"Bitwise left shift moves bits left by {shift} positions: {a} * (2^{shift}) = {res}."

        question = f"What is the result of the Python expression `{expr}`?"
        wrong_options = set()
        while len(wrong_options) < 3:
            offset = random.choice([-2, -1, 1, 2, 4, 8])
            cand = res + offset
            if cand != res and cand >= 0:
                wrong_options.add(cand)

        answers = [{"text": str(res), "is_correct": True}] + [
            {"text": str(w), "is_correct": False} for w in wrong_options
        ]
        random.shuffle(answers)

        return {
            "title": f"Bitwise Expression Evaluation ({op_type})",
            "question": question,
            "difficulty": difficulty,
            "points": 20,
            "time_limit_seconds": 20,
            "explanation": expl,
            "tags": "python,bitwise,operators",
            "answers": answers
        }
