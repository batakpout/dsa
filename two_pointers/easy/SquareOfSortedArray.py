# LC 997 Easy Squares of a Sorted Array

"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    return result



def main():

    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [-5, -4, -3, -2, -1],
        [0],
        [1, 2, 3, 4],
        [-2, -1, 0, 1, 2],
    ]

    for arr in test_cases:
        print(f"Input : {arr}")
        print(f"Output: {sorted_squares(arr)}")
        print("-" * 40)

if __name__ == "__main__":
    main()