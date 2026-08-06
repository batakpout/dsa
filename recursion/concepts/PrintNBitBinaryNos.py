"""

Given a positive integer n, generate all n-bit binary numbers such that, for every prefix of each binary number,
the count of 1's is greater than or equal to the count of 0's.

Return the binary numbers in decreasing order of their decimal value.

Input: n = 3
Output: ["111", "110", "101"]
Explanation: Valid numbers are those where each prefix has more 1s than 0s.
111: all its prefixes (1, 11, and 111) have more 1s than 0s.
110: all its prefixes (1, 11, and 110) have more 1s than 0s.
101: all its prefixes (1, 10, and 101) have more 1s than 0s.
So, the output is "111, 110, 101".

"""

"""
Time : 2^n , will be less and we don't have some branches
Space: O(N) auxillary space, but if we want to count result then
    (number of strings)×(length of each string)=count(n)×n
"""
def print_n_bit_binary_nos(n):
    result = []

    def helper(o, z, n, output):
        if n == 0:
            result.append(output)
            return

        helper(o + 1, z, n - 1, output + "1")
        if   o > z:
            helper(o, z + 1, n - 1, output + "0")

    helper(0, 0, n, "")
    return result

if __name__=="__main__":
    n = int(input("enter a number: "))
    print(print_n_bit_binary_nos(n))
