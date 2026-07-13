#976. Largest Perimeter Triangle LC easy

"""

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of
these lengths. If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:
Input: nums = [2, 3, 4, 5, 6, 7, 8]
output: 21
7 + 6 > 8

Input: nums = [1, 2, 3, 4, 5, 9]
Output: 5
sort : [9, 5, 4, 3, 2, 1]
5+4 not > 9, move to next 5,4,3 i.e 4,3 > 5 -> sum 12

Example 2:

Input: nums = [1,2,1,10]
Output: 0

refer to :-
1. https://sudsy-car-604.notion.site/Triangle-Inequality-theorem-385be6fefaec80ab9383ef34009b6f3b

"""

"""
Now — descending order and why it's "greedy"
Greedy algorithm, in general, means: at each step, make the choice that looks best right now, without reconsidering it later — 
and hope (or prove) that this local choice leads to the global best answer.

For the "maximum perimeter triangle" problem, here's the reasoning:
You want the largest possible perimeter among all valid triangles you can form from the array. The perimeter is just 
a+b+c. So naturally, you want to use the largest numbers available — bigger numbers, bigger perimeter.
Sort descending. Now the biggest numbers are at the front. Try the first three: nums[0], nums[1], nums[2]. 
Check if they form a valid triangle (smallest two > largest, i.e. nums[1] + nums[2] > nums[0]).

If yes — stop. You're done. This must be the best possible answer, because there's no way to get a larger perimeter
 using any other three numbers — these are the three largest numbers in the whole array.
If no — that means nums[0] (the largest number) is too big; it "breaks" with the next two. So you discard nums[0]
 and slide the window down by one: try nums[1], nums[2], nums[3]. Repeat.
"""

#time=O(n log n) space=O(n) for sorting or O(1) if sorting is in place
def largest_perimeter_triangle(nums: list[int]) -> int:
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        a = nums[i]
        b = nums[i + 1]
        c = nums[i + 2]
        if b + c > a:
            return a + b + c
    return 0


if __name__ == "__main__":
    print(largest_perimeter_triangle([2,1,2]))
    print(largest_perimeter_triangle([1,2,1,10]))
    print(largest_perimeter_triangle([1, 2, 3, 4, 5, 9]))
