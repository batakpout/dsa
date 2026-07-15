# LC Easy 643. Maximum Average Subarray I
"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
 Any answer with a calculation error less than 10-5 will be accepted.


Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

"""

from math import inf


def naive(arr, k):
    max_sum = -inf
    n = len(arr)
    for i in range(n - k + 1):
        curr_sum = 0
        for j in range(i, i + k):
            curr_sum += arr[j]
        max_sum = max(curr_sum, max_sum)
    return max_sum / k


def max_average_sliding_window(arr, k):
    window_sum = 0

    # shortcut = window_sum = sum(nums[:k])
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum
    for i in range(k, len(arr)):
        #window_sum = window_sum + arr[i] - arr[i - k]
        window_sum += window_sum + arr[i] - arr[i - k]
        max_sum = max(window_sum, max_sum)
    return max_sum / k


def main():
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4),
        ([5], 1),
        ([5, -10, 6, 90, 3], 2),
        ([0, 4, 0, 3, 2], 1),
        ([-1, -2, -3, -4], 2),
    ]

    for nums, k in test_cases:
        print(f"nums = {nums}")
        print(f"k = {k}")

        print(f"Naive:{naive(nums, k):.5f}")
        print(f"Sliding Window: {max_average_sliding_window(nums, k):.5f}")

        print("-" * 40)


if __name__ == "__main__":
    main()
