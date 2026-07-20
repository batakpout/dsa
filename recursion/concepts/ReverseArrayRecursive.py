"""
* Time: O(n^2)
* Space: O(n) (because of recursion)
"""
def sort_insert(arr: list[int], temp):
    if not arr or arr[-1] <= temp:
        arr.append(temp)
        return

    last = arr.pop()
    sort_insert(arr, temp)
    arr.append(last)


def recursive_sort(arr: list[int]):
    if len(arr) <= 1:
        return

    temp = arr.pop()
    recursive_sort(arr)
    sort_insert(arr, temp)

def main():

    arr = [5, 2, 41, 3]
    print("Before:", arr)
    recursive_sort(arr)
    print("After :", arr)

if __name__ == "__main__":
    main()
