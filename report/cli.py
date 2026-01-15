import argparse
import random
from core.engine import simulate
from strategies import RandomStrategy, CycleStrategy
from .summary import print_summary, save_results


def main():
    parser = argparse.ArgumentParser(description="100 Prisoners Problem Simulator")
    parser.add_argument("--trials", type=int, default=10000, help="Number of trials")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument("--N", type=int, default=100, help="Number of prisoners")
    parser.add_argument("--K", type=int, default=50, help="Max drawers to open")
    parser.add_argument("--out", type=str, default=None, help="Output JSON file path")
    args = parser.parse_args()

    # Random strategy needs its own RNG for drawer selection
    random_rng = random.Random(args.seed)
    random_strategy = RandomStrategy(rng=random_rng)
    cycle_strategy = CycleStrategy()

    wins_random = simulate(random_strategy, args.trials, args.N, args.K, args.seed)
    wins_cycle = simulate(cycle_strategy, args.trials, args.N, args.K, args.seed)

    print_summary(args.trials, wins_random, wins_cycle)

    if args.out:
        save_results(args.out, args.trials, wins_random, wins_cycle, args.N, args.K, args.seed)


if __name__ == "__main__":
    main()
