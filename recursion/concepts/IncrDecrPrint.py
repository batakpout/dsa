def dec(n):
    if n == 0:
        return
    print(n, end=" ")
    dec(n - 1)


def incr(n):
    if n == 0:
        return
    incr(n - 1)
    print(n, end=" ")


if __name__ == "__main__":
    i = 5
    print("Decreasing order:")
    dec(i)
    print("\nIncreasing order:")
    incr(i)
