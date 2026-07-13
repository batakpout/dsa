import random
#from tqdm import tqdm

# Number of trials (large number to approximate the true probability)
N_TRIALS = 10_000_000 #10 million

# Target event: sum of the two dice
TARGET_SUM = 7


def roll_dice():
    """Return a random dice roll between 1 and 6."""
    return random.choice([1, 2, 3, 4, 5, 6])
    # Alternatively:
    # return random.randint(1, 6)


def run_experiment():
    """Roll two dice and return their sum."""
    d1 = roll_dice()
    d2 = roll_dice()
    return d1 + d2


def main():
    n_events = 0

   # for _ in tqdm(range(N_TRIALS)):
    for _ in range(N_TRIALS):
        dice_total = run_experiment()

        if dice_total == TARGET_SUM:
            n_events += 1

    probability = n_events / N_TRIALS

    print(f"\nAfter {N_TRIALS:,} trials:")
    print(f"P(sum = {TARGET_SUM}) ≈ {probability:.6f}")


if __name__ == "__main__":
    main()