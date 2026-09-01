import math
from typing import Tuple, Dict, Any


class EloRatingEngine:
    """
    Authoritative Glicko/Elo competitive rating system for multiplayer matches.
    Calculates expected match win probabilities, dynamic K-factor scaling based on
    player experience, and post-match rating adjustments.
    """

    DEFAULT_RATING = 1200.0
    PROVISIONAL_MATCH_COUNT = 10

    @staticmethod
    def get_dynamic_k_factor(games_played: int, current_rating: float) -> float:
        """
        Determine K-factor:
        - New/provisional players (< 10 matches): K = 40 (rapid placement)
        - Mid-tier players: K = 24
        - Master gladiators (rating > 2000): K = 16 (stability at top rank)
        """
        if games_played < EloRatingEngine.PROVISIONAL_MATCH_COUNT:
            return 40.0
        if current_rating >= 2000.0:
            return 16.0
        return 24.0

    @classmethod
    def calculate_expected_score(cls, rating_a: float, rating_b: float) -> float:
        """Calculate win probability of Player A against Player B: 1 / (1 + 10^((Rb - Ra) / 400))"""
        exponent = (rating_b - rating_a) / 400.0
        return 1.0 / (1.0 + (10.0 ** exponent))

    @classmethod
    def calculate_new_ratings(
        cls,
        rating_a: float,
        rating_b: float,
        games_a: int,
        games_b: int,
        score_a_actual: float  # 1.0 = Win A, 0.5 = Draw, 0.0 = Win B
    ) -> Tuple[float, float, float, float]:
        """
        Calculate new ratings and deltas for 2 players.
        Returns: (new_rating_a, new_rating_b, delta_a, delta_b)
        """
        expected_a = cls.calculate_expected_score(rating_a, rating_b)
        expected_b = 1.0 - expected_a

        k_a = cls.get_dynamic_k_factor(games_a, rating_a)
        k_b = cls.get_dynamic_k_factor(games_b, rating_b)

        score_b_actual = 1.0 - score_a_actual

        delta_a = k_a * (score_a_actual - expected_a)
        delta_b = k_b * (score_b_actual - expected_b)

        new_rating_a = max(100.0, round(rating_a + delta_a, 1))
        new_rating_b = max(100.0, round(rating_b + delta_b, 1))

        return new_rating_a, new_rating_b, round(delta_a, 1), round(delta_b, 1)

    @classmethod
    def get_tier_from_rating(cls, rating: float) -> Dict[str, Any]:
        """Map numeric rating to visual division tier."""
        if rating < 1000:
            return {"tier": "BRONZE", "division": "III", "color": "#cd7f32", "icon": "Shield"}
        elif rating < 1200:
            return {"tier": "BRONZE", "division": "I", "color": "#cd7f32", "icon": "Shield"}
        elif rating < 1400:
            return {"tier": "SILVER", "division": "II", "color": "#c0c0c0", "icon": "Award"}
        elif rating < 1600:
            return {"tier": "GOLD", "division": "I", "color": "#ffd700", "icon": "Trophy"}
        elif rating < 1800:
            return {"tier": "PLATINUM", "division": "I", "color": "#00ffff", "icon": "Zap"}
        elif rating < 2100:
            return {"tier": "DIAMOND", "division": "I", "color": "#b9f2ff", "icon": "Sparkles"}
        else:
            return {"tier": "GRANDMASTER", "division": "ELITE", "color": "#ff0055", "icon": "Crown"}
