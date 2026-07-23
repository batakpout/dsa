# move all from A to B using C

"""
 T(n) = 2T(n-1) + 1 = (2^n)-1 i.e 2ⁿ
 Space = O(N)
"""
def tower_of_hanoi(n, A: str, B: str, C: str):
    if n == 0:
        return
    tower_of_hanoi(n - 1, A, C, B)
    print(f"Moving peg {n} from {A} to {B}")
    tower_of_hanoi(n - 1, C, B, A)


if __name__ == "__main__":
    tower_of_hanoi(3, "A", "B", "C")
