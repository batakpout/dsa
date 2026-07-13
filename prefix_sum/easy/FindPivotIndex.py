#LC 724. Easy Find Pivot Index
"""

 Given an array of integers nums, calculate the pivot index of this array.
 The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
 of all the numbers strictly to the index's right.
 If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
 This also applies to the right edge of the array.
 Return the leftmost pivot index. If no such index exists, return -1.

 Example 1:

 Input: nums = [1,7,3,6,5,6]
 Output: 3
 Explanation:
 The pivot index is 3.
 Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
 Right sum = nums[4] + nums[5] = 5 + 6 = 11

 Example 2:

 Input: nums = [1,2,3]
 Output: -1
 Explanation:
 There is no index that satisfies the conditions in the problem statement.

 Example 3:

 Input: nums = [2,1,-1]
 Output: 0
 Explanation:
 The pivot index is 0.
 Left sum = 0 (no elements to the left of index 0)
 Right sum = nums[1] + nums[2] = 1 + -1 = 0

 """


# naive O(N^2)
def naive(nums: list[int]) -> int:
    for i in range(len(nums)):
        left_sum = 0

        for j in range(0, i):
            left_sum += nums[j]

        right_sum = 0
        for k in range(i + 1, len(nums)):
            right_sum += nums[k]

        if left_sum == right_sum:
            return i
    return -1


# time = O(n) space = O(1)
def optimized(nums: list[int]) -> int:
    right_sum = 0
    for num in nums:
        right_sum += num

    left_sum = 0
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]

    return -1


# time : O(n) + O(n) = O(2n) = O(n) , space = O(n)
def prefix_sum(nums: list[int]) -> int:
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]

    total_sum = prefix[-1]
    for i in range(n):
        left_sum = 0 if i == 0 else prefix[i - 1]
        right_sum = total_sum - prefix[i]
        if left_sum == right_sum:
            return i
    return -1


if __name__ == "__main__":
    nums1 = [1, 7, 3, 6, 5, 6]
    print(naive(nums1))
    print(optimized(nums1))
    print(prefix_sum(nums1))

    nums2 = [2, 1, -1]
    print(naive(nums2))
    print(optimized(nums2))
    print(prefix_sum(nums2))

    num3 = [1, 2, 3]
    print(naive(num3))
    print(optimized(num3))
    print(prefix_sum(num3))

    num4 = [8, -3, 2, 1, -6, 4, 0, 2, -2, 6]
    print(naive(num4))
    print(optimized(num4))
    print(prefix_sum(num4))
