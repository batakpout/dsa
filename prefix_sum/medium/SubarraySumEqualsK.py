#560. Medium Subarray Sum Equals K
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""

"""

The whole algorithm in words

lets start with what you want
You're at some index i. You want to know: is there a subarray ending exactly here that sums to k?
A subarray ending at i means: it starts at some j where j <= i, and covers nums[j..i].
So the question becomes: for which values of j does nums[j..i] = k?

Prefix sum enters naturally
Computing nums[j..i] by looping is expensive. But you already know:
nums[j..i] = prefix[i] - prefix[j-1]
So the condition nums[j..i] = k becomes:
prefix[i] - prefix[j-1] = k
Rearrange:
prefix[j-1] = prefix[i] - k
Now read this slowly. You're standing at index i. You already know prefix[i]. You already know k. So prefix[i] - k is
 just a number — call it target.
The question "does a valid subarray end here?" has become: "Did I ever see the value target as a prefix sum, somewhere before index i?"


That's the entire insight
You're not searching through subarrays anymore. You're not doing nested loops. You just need to answer one question per index:

"Have I seen this specific prefix sum value before?"

And a hashmap answers that in O(1).

why we need hashmap?

## Concrete example where set fails

```
nums = [11, 2, -2, 0, 3]   k = 3
```

Prefix sums: `[11, 13, 11, 11, 14]`

With your set approach:

```
set = {0}
count = 0
```

| i | prefix | diff=prefix-k | in set? | count | set after |
|---|--------|----------------|---------|-------|-----------|
| 0 | 11     | 8              | no      | 0     | {0, 11}   |
| 1 | 13     | 10             | no      | 0     | {0, 11, 13} |
| 2 | 11     | 8              | no      | 0     | {0, 11, 13} ← 11 already there, set doesn't change |
| 3 | 11     | 8              | no      | 0     | {0, 11, 13} ← same |
| 4 | 14     | 11             | **yes** | 1     | {0, 11, 13, 14} |

**Set gives `count = 1`. Wrong.**

The map gives `count = 3` because `seen[11] = 3` at index 4 — three earlier indices had prefix sum `11`, 
meaning three distinct subarrays end at index 4 and sum to `k`.

---

## Why the set loses information

When prefix sum `11` appears at index 0, index 2, and index 3 — the set just stores `11` once. 
It collapses three distinct events into one. It can only tell you "yes, 11 existed somewhere before" —
 not "11 existed at 3 different points, each representing a different valid left boundary."

The map stores `11 → 3`, preserving exactly how many left boundaries had that prefix sum.

---

## One line summary

> A set answers **"did I see X?"** — a map answers **"how many times did I see X?"** — and you need the count because 
each occurrence of a repeated prefix sum is a *separate, distinct* valid subarray.
"""


# This takes O(n²) time because there are approximately n(n+1)/2 subarrays.
def prefix_sum(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]
    counter = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = prefix[j] if i == 0 else prefix[j] - prefix[i - 1]
            if current_sum == k:
                counter += 1
    return counter

#above approach sucks, simple brute force O(n^2)
def brute_force(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)
    for start in range(n):
        total = 0
        for end in range(start, n):
            total += nums[end]
            if total == k:
                count += 1
    return count

# space = O(n), time = O(n)
def optimized(nums: list[int], k: int):
    seen: dict[int, int] = {0: 1}

    prefix = 0
    count = 0
    for i, num in enumerate(nums):
        prefix += num
        diff = prefix - k
        if diff in seen:
            count += seen[diff]
        seen[prefix] = seen.get(prefix, 0) + 1

    return count


if __name__ == "__main__":
    nums1 = [1, 1, 1]
    k1 = 2
    print(prefix_sum(nums1, k1))
    print(optimized(nums1, k1))

    nums2 = [1, 2, 3]
    k2 = 3
    print(prefix_sum(nums2, k2))
    print(optimized(nums2, k2))

    print("____")
    nums3 = [1, -1, 1, -1, 1]
    k3 = 1
    print(optimized(nums3, k3))

    nums4 = [1, 2, 1, 2]
    k4 = 3
    print(optimized(nums4, k4))
