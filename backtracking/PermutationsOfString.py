def using_recursion(s: str) -> list[str]:
    result = []

    def helper(input, output):
        if not input:
            result.append(output)
            return
        seen = set()
        for i, ch in enumerate(input):
            if ch in seen:
                continue

            seen.add(ch)
            helper(input[:i] + input[i + 1:], output + ch)

    helper(s, "")
    return result


if __name__ == "__main__":
    input = input("enter a string:-")
    print(using_recursion(input))
