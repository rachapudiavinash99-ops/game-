import math
from typing import Dict, Any


class ScoringEngine:
    BASE_SCORES = {
        "EASY": 10,
        "MEDIUM": 20,
        "HARD": 35,
        "EXPERT": 50
    }

    SPEED_BONUS_MAX = 15  # Max bonus points for answering fast

    @classmethod
    def calculate_question_score(
        cls,
        difficulty: str,
        is_correct: bool,
        time_spent_seconds: float,
        time_limit_seconds: float,
        current_streak: int
    ) -> Dict[str, Any]:
        """
        Authoritative calculation of points for a single question.
        Includes base score by difficulty, speed bonus, and streak multiplier.
        """
        if not is_correct:
            return {
                "points": 0,
                "base_points": 0,
                "speed_bonus": 0,
                "streak_bonus": 0,
                "multiplier": 1.0
            }

        diff_key = difficulty.upper() if difficulty else "MEDIUM"
        base_points = cls.BASE_SCORES.get(diff_key, 20)

        # Speed bonus: faster answer yields higher bonus
        time_ratio = max(0.0, min(1.0, (time_limit_seconds - time_spent_seconds) / max(1.0, time_limit_seconds)))
        speed_bonus = int(round(time_ratio * cls.SPEED_BONUS_MAX))

        # Streak multiplier: +10% per streak level up to 2.5x (streak of 15+)
        streak_multiplier = min(2.5, 1.0 + (max(0, current_streak) * 0.1))
        
        raw_points = (base_points + speed_bonus) * streak_multiplier
        final_points = int(math.ceil(raw_points))

        return {
            "points": final_points,
            "base_points": base_points,
            "speed_bonus": speed_bonus,
            "streak_bonus": int(final_points - base_points - speed_bonus),
            "multiplier": round(streak_multiplier, 2)
        }

    @classmethod
    def calculate_xp_earned(cls, score: int, accuracy: float, mode: str) -> int:
        """Calculate player XP reward based on score, accuracy, and game mode."""
        mode_multipliers = {
            "QUICK_CHALLENGE": 1.0,
            "TOPIC_CHALLENGE": 1.2,
            "TIME_ATTACK": 1.4,
            "SURVIVAL": 1.5,
            "MULTIPLAYER": 1.6
        }
        mult = mode_multipliers.get(mode, 1.0)
        # Accuracy bonus between 1.0x and 1.5x
        acc_bonus = 1.0 + (accuracy / 200.0)
        xp = int(round((score * 0.5) * mult * acc_bonus))
        return max(10, xp)
