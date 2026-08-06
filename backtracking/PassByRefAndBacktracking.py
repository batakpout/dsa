def print_array(arr):
    print(arr)


def fill_array(arr, i, n, val): # arr by default call by reference
    if i == n:
        print_array(arr)
        return

    arr[i] = val
    fill_array(arr, i + 1, n, val+1)
    arr[i] = -arr[i] #this is backtracking step
    return


if __name__ == "__main__":
    n = 5
    arr =[0]  * 5
    fill_array(arr, 0, n, 1)
    print_array(arr)
