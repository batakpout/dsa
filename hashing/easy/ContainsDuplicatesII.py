# LC 219 [has solution in sliding window also, and use that one as that is space optimized]

"""
Time O(n)

Space O(n)
from ContainsDuplicatesII from sliding window, here hashing solution
"""
def contains_duplicates(k: int, nums: list[int]) -> bool:
    nums_dict: dict[int, int] = {}
    for i, num in enumerate(nums):
        if num in nums_dict and (i - nums_dict[num] <= k):
            return True
        else:
            nums_dict[num] = i
    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1, 2, 3, 1, 2, 1, 3]
    k1 = 2
    print(contains_duplicates(k1, nums1))

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(contains_duplicates(k, nums))
