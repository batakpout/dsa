# Python passes lists by reference (similar to C++)

def insert_at_bottom(stack: list[int], data_to_insert: int):
    if not stack:
        stack.append(data_to_insert)
        return None
    top = stack[-1]
    stack.pop()
    insert_at_bottom(stack, data_to_insert)
    stack.append(top)
    return stack


"""
reversed(stack) does not reverse the list.
It returns an iterator that lets you iterate over the list from the last element to the first.
"""
def display_stack(stack: list[int]):

    print("Top")
    print("  ---")
    for item in reversed(stack):
        print(f"| {item} |")
    print("  ---")
    print("Bottom")

def main():

    stack = [10, 20, 30, 40]   # 40 is the top of the stack
    print("Original Stack:")
    display_stack(stack)
    data = 5
    print(f"\nInserting {data} at the bottom...\n")

    insert_at_bottom(stack, data)

    print("Stack After Insertion:")
    display_stack(stack)

if __name__ == "__main__":

    main()
