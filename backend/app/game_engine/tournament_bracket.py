import math
import random
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class MatchParticipant:
    user_id: int
    username: str
    seed: int
    score: int = 0
    is_winner: bool = False


@dataclass
class TournamentMatch:
    match_id: str
    round_number: int
    match_index: int
    player_1: Optional[MatchParticipant] = None
    player_2: Optional[MatchParticipant] = None
    winner_id: Optional[int] = None
    is_completed: bool = False
    next_match_id: Optional[str] = None


class TournamentBracketEngine:
    """
    Deterministic tournament generation engine supporting:
    - Single elimination bracket trees
    - Power-of-2 padding with automated 'Bye' seeds
    - Swiss system round pairings based on dynamic match scores
    """

    @classmethod
    def generate_single_elimination(cls, players: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate a complete single-elimination tournament structure.
        Pairs highest seed with lowest seed in classic standard bracket format.
        """
        num_players = len(players)
        if num_players < 2:
            return {"error": "Minimum 2 players required"}

        # Next power of 2
        power = math.ceil(math.log2(num_players))
        bracket_size = 2 ** power
        total_rounds = power

        # Seed players
        sorted_players = sorted(players, key=lambda p: p.get("rating", 1200), reverse=True)
        participants: List[Optional[MatchParticipant]] = []
        for i in range(bracket_size):
            if i < num_players:
                p = sorted_players[i]
                participants.append(MatchParticipant(user_id=p["user_id"], username=p["username"], seed=i + 1))
            else:
                participants.append(None)  # Bye

        # Standard seeding order algorithm (1 vs 16, 8 vs 9, etc.)
        def get_seed_order(size: int) -> List[int]:
            bracket = [1, 2]
            while len(bracket) < size:
                next_bracket = []
                target = len(bracket) * 2 + 1
                for seed in bracket:
                    next_bracket.append(seed)
                    next_bracket.append(target - seed)
                bracket = next_bracket
            return bracket

        seed_indices = get_seed_order(bracket_size)
        ordered_participants = []
        for s in seed_indices:
            idx = s - 1
            ordered_participants.append(participants[idx] if idx < len(participants) else None)

        rounds_dict: Dict[int, List[TournamentMatch]] = {r: [] for r in range(1, total_rounds + 1)}

        # Round 1 matches
        r1_match_count = bracket_size // 2
        for m_idx in range(r1_match_count):
            p1 = ordered_participants[m_idx * 2]
            p2 = ordered_participants[m_idx * 2 + 1]

            match_id = f"R1_M{m_idx + 1}"
            next_m_id = f"R2_M{(m_idx // 2) + 1}" if total_rounds > 1 else None

            match = TournamentMatch(
                match_id=match_id,
                round_number=1,
                match_index=m_idx + 1,
                player_1=p1,
                player_2=p2,
                next_match_id=next_m_id
            )

            # Auto advance if Bye
            if p1 and not p2:
                match.winner_id = p1.user_id
                match.is_completed = True
                p1.is_winner = True
            elif p2 and not p1:
                match.winner_id = p2.user_id
                match.is_completed = True
                p2.is_winner = True

            rounds_dict[1].append(match)

        # Build subsequent round placeholder matches
        for r in range(2, total_rounds + 1):
            matches_in_round = bracket_size // (2 ** r)
            for m_idx in range(matches_in_round):
                match_id = f"R{r}_M{m_idx + 1}"
                next_m_id = f"R{r + 1}_M{(m_idx // 2) + 1}" if r < total_rounds else None
                match = TournamentMatch(
                    match_id=match_id,
                    round_number=r,
                    match_index=m_idx + 1,
                    next_match_id=next_m_id
                )
                rounds_dict[r].append(match)

        return {
            "bracket_size": bracket_size,
            "total_rounds": total_rounds,
            "rounds": {
                r: [
                    {
                        "match_id": m.match_id,
                        "round": m.round_number,
                        "player_1": {"user_id": m.player_1.user_id, "username": m.player_1.username, "seed": m.player_1.seed} if m.player_1 else None,
                        "player_2": {"user_id": m.player_2.user_id, "username": m.player_2.username, "seed": m.player_2.seed} if m.player_2 else None,
                        "winner_id": m.winner_id,
                        "is_completed": m.is_completed,
                        "next_match_id": m.next_match_id
                    }
                    for m in matches
                ]
                for r, matches in rounds_dict.items()
            }
        }
