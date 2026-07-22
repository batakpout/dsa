def insert_at_bottom(stack: list[int], data_to_insert: int):
    if not stack:
        stack.append(data_to_insert)
        return None
    top = stack[-1]
    stack.pop()
    insert_at_bottom(stack, data_to_insert)
    stack.append(top)
    return stack


def reverse(stack: list[int]):
    if not stack:
        return stack
    top = stack.pop()
    reverse(stack)
    return insert_at_bottom(stack, top)

def display_stack(stack: list[int]):

    print("Top")
    print("  ---  ")
    for item in reversed(stack):

        print(f"| {item} |")

    print("  ---  ")

    print("Bottom")

def main():

    stack = [42, 22, 50, 33]    # Last element is the top of the stack 40

    print("Original Stack:")
    display_stack(stack)
    reverse(stack)
    print("\nReversed Stack:")
    display_stack(stack)

if __name__ == "__main__":

    main()