# LeetCode 1 [has two pointer solution also]
"""
Space = O(n)
Time = n iterations × O(1) work per iteration = O(n)
"""
def using_dictionary(target:int, nums:list[int]) -> list[int]:
    seen = {} # a dictionary
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return [-1,-1]


if __name__ == "__main__":
    nums1 = [2, 3, 6, 7, 11, 9, 16]
    target1 = 15
    print(using_dictionary(target1, nums1))

    nums2 = [2, 21, 3, 12, 4]
    target2 = 6
    print(using_dictionary(target2, nums2))

    nums3 = [3, 32,2,1,]
    target3 = 8
    print(using_dictionary(target3, nums3))