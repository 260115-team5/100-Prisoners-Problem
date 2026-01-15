import json
from datetime import datetime
from typing import Optional


def print_summary(
    trials: int,
    wins_random: int,
    wins_cycle: int
) -> None:
    p_random = wins_random / trials if trials > 0 else 0
    p_cycle = wins_cycle / trials if trials > 0 else 0
    print(f"Random Strategy:  wins={wins_random}/{trials},    p={p_random:.4f}")
    print(f"Cycle Strategy:   wins={wins_cycle}/{trials}, p={p_cycle:.4f}")


def save_results(
    filepath: str,
    trials: int,
    wins_random: int,
    wins_cycle: int,
    n: int,
    k: int,
    seed: Optional[int]
) -> None:
    data = {
        "trials": trials,
        "wins_random": wins_random,
        "p_random": wins_random / trials if trials > 0 else 0,
        "wins_cycle": wins_cycle,
        "p_cycle": wins_cycle / trials if trials > 0 else 0,
        "N": n,
        "K": k,
        "seed": seed,
        "timestamp": datetime.now().isoformat()
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Results saved to {filepath}")
