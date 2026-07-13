#LC 674. Easy Longest Continuous Increasing Subsequence

"""
For an array of size n, the number of consecutive (contiguous) subarrays is: n(n+1)/2 Why?
Index 0 → n subarrays
Index 1 → n-1 subarrays
Index 2 → n-2 subarrays
...
Index n-1 → 1 subarray [i.e if n = 4, last one is index = 3 i.e n-1

Total number of consecutive subarrays
n + (n - 1) + (n - 2) + ... + 2 + 1 = n(n + 1) / 2

for [1,2,3]
[1]
[1,2]
[1,2,3]

[2]
[2,3]

[3]

Total = 6
"""

"""
nums = [5, 7, 9, 2, 3, 4, 8, 1, 2, 3, 4, 5, 0, 6]
output = 5 sub array: [1,2,3,4,5]

nums = [2,2,2]
output = 1
"""

"""
Time: O(N)
Space = O(1)
"""

def large_continuous_increasing_sub_sequence(nums: list[int]) -> int:
    if not nums:
        return 0
    max_length = 0
    current_length = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    return max(max_length, current_length)


if __name__ == "__main__":
    nums = [1,3,5,4,7]
    print(large_continuous_increasing_sub_sequence(nums))
