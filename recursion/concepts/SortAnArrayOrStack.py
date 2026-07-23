def insert(stack: list[int], temp: int) -> None:
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return

    val = stack.pop()
    insert(stack, temp)
    stack.append(val)


def sort(stack: list[int], n: int) -> None:
    if n <= 1:
        return

    temp = stack.pop()
    sort(stack, n - 1)
    insert(stack, temp)


if __name__ == "__main__":
    stack = [5, 1, 4, 2, 8, 3]

    print("Original Stack :", stack)

    sort(stack, len(stack))

    print("Sorted Stack   :", stack)