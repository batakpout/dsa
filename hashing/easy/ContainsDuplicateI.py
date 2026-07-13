#LC Easy 217

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true



"""
"""
Time Complexity = O(n)
Space Complexity = O(n)
"""
def contains_duplicate(nums: list[int]) -> bool:

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

"""
Time Complexity = O(n log n)
Space Complexity = O(1)
"""

def using_sort(nums: list[int]) -> bool:
    sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
"""
In interviews:
* If asked for the fastest solution → use set.
* If asked to optimize space → use sorting.
"""

def main():

    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 1]
    arr3 = [5, 5, 5, 5]
    arr4 = []
    arr5 = [10]

    print(f"{arr1} -> {contains_duplicate(arr1)}")
    print(f"{arr2} -> {contains_duplicate(arr2)}")
    print(f"{arr3} -> {contains_duplicate(arr3)}")
    print(f"{arr4} -> {contains_duplicate(arr4)}")
    print(f"{arr5} -> {contains_duplicate(arr5)}")

if __name__ == "__main__":
    main()