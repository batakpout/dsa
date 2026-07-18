"""
Bubble Sort:
Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
After each pass, the largest unsorted element "bubbles" to its correct position at the end.

Dry Run: [5, 3, 8, 4, 2]

Pass 1:
5 3 8 4 2
5 > 3 -> swap -> [3, 5, 8, 4, 2]
5 < 8 -> no swap
8 > 4 -> swap -> [3, 5, 4, 8, 2]
8 > 2 -> swap -> [3, 5, 4, 2, 8]

Pass 2:
[3, 5, 4, 2, 8]
3 < 5 -> no swap
5 > 4 -> swap -> [3, 4, 5, 2, 8]
5 > 2 -> swap -> [3, 4, 2, 5, 8]

Pass 3:
[3, 4, 2, 5, 8]
3 < 4 -> no swap
4 > 2 -> swap -> [3, 2, 4, 5, 8]

Pass 4:
[3, 2, 4, 5, 8]
3 > 2 -> swap -> [2, 3, 4, 5, 8]

Sorted Array:
[2, 3, 4, 5, 8]

Time Complexity:
Best:    O(n)   (with early exit optimization)
Average: O(n²)
Worst:   O(n²)

Space Complexity:
O(1)
"""


def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


"""
Recursive Bubble Sort
Idea:
- One pass bubbles the largest element to the end.
- Recursively sort the remaining first n-1 elements.
Time Complexity:
Best:    O(n)   (with early exit optimization)
Average: O(n²)
Worst:   O(n²)
Space Complexity:O(n) due to recursive call stack.
"""


def one_pass(arr: list[int], j, n) -> bool:
    if j >= n - 1:
        return False
    swapped_here = False
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped_here = True
    swapped_rest = one_pass(arr, j + 1, n)
    """
    why we need swapper_here in return
    swapped_rest only knows about pairs after the current one (j+1 onward). It has zero information about what happened
    at index j itself. If you return just swapped_rest, you silently throw away that information.
    e.g input is 2,1,4,5,6 for current stack frame it is True, for all other it is False, so we should return True
    so yes we returned as we had this statement in here
    """
    return swapped_here or swapped_rest


def recursive_bubble_sort(arr: list[int], n=None) -> list[int]:
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr

    swapped = one_pass(arr, 0, n)
    if not swapped:
        return arr
    return recursive_bubble_sort(arr, n - 1)


if __name__ == "__main__":
    test_cases = [
        [5, 3, 8, 4, 2],  # Random order
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [7],  # Single element
        [],  # Empty list
        [4, 2, 4, 1, 2]  # Duplicates
    ]

    for arr in test_cases:
        print(f"Original: {arr}")
        # print(f"Sorted:   {bubble_sort(arr.copy())}")  # copy creates another list
        print(f"Sorted:   {recursive_bubble_sort(arr.copy())}")  # copy creates another list
        print("-" * 30)
