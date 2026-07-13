def first_occ(arr, n, key):
    if n == 0:
        return -1
    if arr[0] == key:
        return 0
    sub_index = first_occ(arr[1:], n - 1, key)

    if sub_index != -1:
        return sub_index + 1
    return -1


def last_occ(arr, n, key):
    if n == 0:
        return -1
    sub_index = last_occ(arr[1:], n - 1, key)
    if sub_index == -1:
        if arr[0] == key:
            return 0
        else:
            return -1
    else:
        return sub_index + 1


def find_all_occurrences(key, arr):
    result = []
    n = len(arr)

    def helper(idx):
        if idx == n:
            return
        if arr[idx] == key:
            result.append(idx)

        helper(idx + 1)

    helper(0)
    return result


if __name__ == "__main__":
    n = int(input("Enter the number of array elements:\n"))
    arr = []
    print(f"Enter {n} array elements:\n")
    for i in range(n):
        arr.append(int(input()))
    key = int(input("Enter the key to search:\n"))
    index = first_occ(arr, n, key)

    if index != -1:
        print(f"first occ of {key} is at index {index}.")
    else:
        print(f"{key} not found in the array")

    last_index = last_occ(arr, n, key)

    if last_index != -1:
        print(f"last occ of {key} is at index {last_index}.")
    else:
        print(f"{key} not found in the array")

    all_occur = find_all_occurrences(key, arr)

    if all_occur:
        print("Key found at indices:", all_occur)
    else:
        print("Key not found.")
