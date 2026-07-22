import random


def play():
    num_games = 100_000
    second_player_wins = 0
    for _ in range(num_games):
        S = 0
        while S <= 100:
            x = random.randint(1, 100)  # [1,100] closed interval
            print(f"x = {x}")
            S += x
        while S <= 200:
            y = random.randint(1, 100)
            print(f"y = {y}")
            S += y
        print("y big") if y > x else print("x big")
        if y > x:
            second_player_wins += 1

    probability = second_player_wins / num_games
    print(f"Estimated probability that the second player wins: {probability:.5f}")
#This is a Monte Carlo simulation, where we estimate a probability by running the experiment many times.

if __name__ == "__main__":
    play()
