import math
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class KeystrokeTiming:
    key_code: str
    down_time_ms: float
    up_time_ms: float
    dwell_time_ms: float = field(init=False)

    def __post_init__(self):
        self.dwell_time_ms = max(0.0, self.up_time_ms - self.down_time_ms)


@dataclass
class PlayerResponseTelemetry:
    user_id: int
    task_id: int
    presented_at_ms: float
    answered_at_ms: float
    time_spent_seconds: float
    keystrokes: List[KeystrokeTiming] = field(default_factory=list)
    pointer_movements: List[Dict[str, float]] = field(default_factory=list)
    client_clock_drift_ms: float = 0.0


class AntiCheatEngine:
    """
    Server-authoritative heuristic anti-cheat system.
    Evaluates response latencies, superhuman reaction thresholds, input anomalies,
    and bot timing signatures without client-side trusting.
    """

    # Minimum human reading & reaction threshold in milliseconds (sub-human reaction alert)
    MIN_HUMAN_REACTION_MS = 280.0
    # Minimum reading speed: approx 600 words per minute max for comprehension
    MAX_WORDS_PER_SECOND = 15.0

    @classmethod
    def calculate_question_word_count(cls, question_text: str) -> int:
        """Count words in question body to estimate minimum reading time."""
        if not question_text:
            return 0
        return len(question_text.split())

    @classmethod
    def estimate_minimum_reading_time_ms(cls, question_text: str, answer_count: int = 4) -> float:
        """
        Estimate physically minimum time needed for a human to read the question
        and inspect the multiple choice answers.
        """
        words = cls.calculate_question_word_count(question_text) + (answer_count * 5)
        reading_ms = (words / cls.MAX_WORDS_PER_SECOND) * 1000.0
        return cls.MIN_HUMAN_REACTION_MS + reading_ms

    @classmethod
    def evaluate_telemetry(
        cls,
        telemetry: PlayerResponseTelemetry,
        question_text: str,
        difficulty: str
    ) -> Dict[str, Any]:
        """
        Analyze submission latency and telemetry signatures.
        Returns suspiciousness rating (0.0 = completely clean, 1.0 = highly suspicious / automated).
        """
        anomalies = []
        suspicion_score = 0.0

        latency_ms = telemetry.time_spent_seconds * 1000.0
        min_expected_ms = cls.estimate_minimum_reading_time_ms(question_text)

        # 1. Superhuman latency check
        if latency_ms < cls.MIN_HUMAN_REACTION_MS:
            anomalies.append("SUB_HUMAN_REACTION_TIME")
            suspicion_score += 0.75
        elif latency_ms < (min_expected_ms * 0.35) and difficulty in ("HARD", "EXPERT"):
            anomalies.append("IMPROBABLE_READING_SPEED_FOR_COMPLEXITY")
            suspicion_score += 0.45

        # 2. Timing consistency check (bots often have flat distribution variance)
        if len(telemetry.keystrokes) >= 3:
            dwell_times = [k.dwell_time_ms for k in telemetry.keystrokes]
            avg_dwell = sum(dwell_times) / len(dwell_times)
            variance = sum((d - avg_dwell) ** 2 for d in dwell_times) / len(dwell_times)
            std_dev = math.sqrt(variance)

            # Artificial robot typing has virtually zero dwell variance
            if std_dev < 1.5:
                anomalies.append("ZERO_VARIANCE_ARTIFICIAL_TYPING")
                suspicion_score += 0.50

        # 3. Client clock tampering check
        if abs(telemetry.client_clock_drift_ms) > 5000.0:
            anomalies.append("SIGNIFICANT_CLIENT_CLOCK_DRIFT")
            suspicion_score += 0.30

        return {
            "is_flagged": suspicion_score >= 0.70,
            "suspicion_score": min(1.0, round(suspicion_score, 2)),
            "latency_ms": round(latency_ms, 1),
            "min_expected_ms": round(min_expected_ms, 1),
            "anomalies": anomalies,
            "verified_at": time.time()
        }
