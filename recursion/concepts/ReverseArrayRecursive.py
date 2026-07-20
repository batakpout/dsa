"""
reverse a stack
"""

def insert_at_bottom(stack: list[int], data_to_insert: int):
    if not stack:
        stack.append(data_to_insert)
        return None
    top = stack[-1]
    stack.pop()
    insert_at_bottom(stack, data_to_insert)
    stack.append(top)
    return stack


def sort_stack(stack: list[int]):
    if not stack:
        return
    top = stack[-1]
    stack.pop()
    sort_stack(stack)
    insert_at_bottom(stack, top)

def display_stack(stack: list[int]):

    print("Top")
    print("  ---")
    for item in reversed(stack):
        print(f"| {item} |")
    print("  ---")
    print("Bottom")

def main():

    stack = [40, 30, 20, 10]  # 10 is the top of the stack
    print("Original Stack:")
    display_stack(stack)
    print(f"\nsorted stack\n")

    sort_stack(stack)

    display_stack(stack)

if __name__ == "__main__":
    main()