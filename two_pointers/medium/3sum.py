# LC 15 medium 3Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
 and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

"""
Intuition:
If we’ve already used -1 as the first element, using another identical -1 as the first element cannot produce any new 
unique triplets, so sorting avoids duplicates then.

we need inner duplicate check for inputs
[-2, 0, 0, 0, 0, 2]
[-2, 0, 2, 2, 2]
[-2, 0, 0, 2, 2]
if we set -2, then we find 2, then we ensure we don't put duplicates in output
"""

"""
3Sum - Why do we only search to the RIGHT of i?

Walkthrough with your array:
Index: 0   1   2   3   4   5
Value:-5  -3  -1   2   4   6
Say the valid triplet is [-3, -1, 4] at indices 1, 2, 4.

When i = 1 (value -3): you search right, with left = 2, right = 5. 
Two-pointer narrows down and finds (-3, -1, 4). ✅ Caught here.

When i = 2 (value -1): could you find this same triplet by looking left to index 1? Technically yes, the numbers are
 there — but it's the same three numbers, just discovered a second time. That's a duplicate, not a new answer.

"""

"""
Time complexity:
 - Sorting: O(n log n)
 - Outer loop runs O(n) times, and for each iteration the inner two-pointer loop does O(n) work (left and right pointers
   together traverse the remaining array once).
 - Total: O(n) × O(n) = O(n²), which dominates the O(n log n) sort.
 - So, TC = O(n²) [three_sum can't be solved faster than O(n²) with known techniques]

Space-complexity:
 - Auxiliary Space Complexity: O(1) (excluding the output list) or O(log n) to O(n) (due to sort) 
 - The result list is typically not counted as "extra" space since it's the required output, but if you do count it, 
   it can hold up to O(n²) triplets in the worst case. then O(n²).
 
   
"""


def three_sum(nums: list[int]):
    result = []
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s > 0:
                right -= 1
            elif s < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


def main():
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0, 0],
        [-2, 0, 0, 2, 2],
        [-2, 0, 1, 1, 2],
        [-1, 0, 1, 2, -1, -4]
    ]

    for nums in test_cases:
        print(f"Input : {nums}")
        print(f"Output: {three_sum(nums.copy())}")
        print("-" * 40)


if __name__ == "__main__":
    main()
