# LC 1200. Easy Minimum Absolute Difference
"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106

"""

"""
time complexity: O(n log n) + O(n) = O(n log n), log grows faster than linear scanning as input size scales
space complexity: O(n)
"""


def minimum_abs_difference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    result: list[list[int]] = []
    # result  = [[]]
    min_diff = float('inf')  # infinite max nummber

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = [[arr[i - 1], arr[i]]]
        elif diff == min_diff:
            result.append([arr[i - 1], arr[i]])
    return result


if __name__ == "__main__":
    arr1 = [4, 2, 1, 3]
    res1 = minimum_abs_difference(arr1)
    print(res1)

    arr2 = [1, 3, 6, 10, 15]
    res2 = minimum_abs_difference(arr2)
    print(res2)

    arr3 = [3, 8, -10, 23, 19, -4, -14, 27]
    res3 = minimum_abs_difference(arr3)
    print(res3)
