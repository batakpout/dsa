"""
Complexity
* Time: O(n)
* Space: O(n) (recursive call stack)
"""
def delete_kth_element(stack: list[int], k: int):
    if k == 1:
        stack.pop()
        return stack
    top = stack.pop()
    delete_kth_element(stack, k - 1)
    return stack.append(top)


def delete_middle_element(stack: list[int]):
    if not stack:
        return stack
    k = len(stack) // 2 + 1
    return delete_kth_element(stack, k)

def display_stack(stack: list[int]):
    print("Top")
    print("  ----  ")
    for item in reversed(stack):
        print(f"| {item} |")
    print("  ----  ")
    print("Bottom")

def main():


    stack = [5, 10, 20, 30, 40, 50]    # Last element is the top of the stack 50

    print("=" * 35)
    print("Original Stack")
    print("=" * 35)
    display_stack(stack)
    delete_middle_element(stack)
    print("\n" + "=" * 35)

    print("After Deleting Middle Element")
    print("=" * 35)
    display_stack(stack)
    print("\nUnderlying Python List:")
    print(stack)

if __name__ == "__main__":
    main()