#LC 88 easy Merge Sorted Array

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


"""
"""
* Time Complexity: O(m + n)
    * Each element from nums1 and nums2 is examined at most once.
* Space Complexity: O(1)
    * The merge is performed in-place using only a few pointers.
"""

"""
 we can just merge both, and sort them that would be O(n log n )
"""
#list1 will be of size list1+list2
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >=0 and p2 >=0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

    while p2  >=0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0] #zeros are empty slots
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    print("Test 1:", nums1)

    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 3, nums2, 3)
    print("Test 2:", nums1)

    nums1 = [1, 2, 3, 4, 5, 6, 0, 0, 0, 0]
    nums2 = [2, 3, 4, 5]
    merge(nums1, 6, nums2, 4)     # fix: m=6 not 10
    print("Test 3:", nums1)        # [1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
