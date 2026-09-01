from app.services.scoring_engine import ScoringEngine
from app.services.progression_service import ProgressionService


def test_scoring_engine_correct_answer_speed_bonus():
    calc = ScoringEngine.calculate_question_score(
        difficulty="HARD",
        is_correct=True,
        time_spent_seconds=2.0,
        time_limit_seconds=20.0,
        current_streak=3
    )
    assert calc["points"] > 35  # Base is 35 + speed bonus + streak
    assert calc["base_points"] == 35
    assert calc["speed_bonus"] > 0
    assert calc["multiplier"] == 1.3


def test_scoring_engine_incorrect_answer():
    calc = ScoringEngine.calculate_question_score(
        difficulty="EXPERT",
        is_correct=False,
        time_spent_seconds=10.0,
        time_limit_seconds=20.0,
        current_streak=5
    )
    assert calc["points"] == 0
    assert calc["base_points"] == 0


def test_progression_level_formula():
    lvl_1_xp = ProgressionService.get_xp_for_level(1)
    lvl_2_xp = ProgressionService.get_xp_for_level(2)
    lvl_5_xp = ProgressionService.get_xp_for_level(5)
    assert lvl_1_xp == 100
    assert lvl_2_xp > lvl_1_xp
    assert lvl_5_xp > lvl_2_xp
