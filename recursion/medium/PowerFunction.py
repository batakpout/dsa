# 50. Pow(x, n) Medium
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""

# try lc 50, 231, 372, 326
"""
Time = O(N)
Space = O(N)
"""


def power(base, pow):
    if pow == 0:
        return 1
    return base * power(base, pow - 1)


"""
Time = O(Log(N))
Space = O(Log(N))
Log(N) means log base 2 of input power
"""


def optimized(base, power):
    if power == 0: return 1
    if base == 0: return 0

    def helper(base, power):
        if power == 0:
            return 1
        sub_pow = helper(base, power // 2)
        if power % 2 == 0:
            return sub_pow * sub_pow
        else:
            return base * sub_pow * sub_pow

    result = helper(base, abs(power))
    return result if power > 0 else 1/result


if __name__ == "__main__":
    print(power(3, 3))
    print(power(2, 10))
    print(power(5, 3))

    print(optimized(3, 3))
    print(optimized(2, 10))
    print(optimized(5, 3))
    print(optimized(2, -2))
