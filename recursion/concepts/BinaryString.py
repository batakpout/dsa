"""
why f(0) = 1
n = 0, How many binary strings have length  == 0?  There is only one: "", It contains no consecutive 1s
 (it contains nothing at all). So f(0) = 1

 Time complexity: O(2^N) like fibo. With DP O(N) , with matrix exponentiation O(K^3 log(N)).
 k is no os steps in recurrence e.g in T(n) = T(n-1) + T(n-2), k = 3
"""

"""
Binary Strings!
You are given an integer N. Your task is to print all binary strings of size N without consecutive ones.

Constraints:

N<=12

Input Format

In the given function an integer N is passed as parameter.

Output Format

Return a vector of strings, with all possible strings in a sorted order.



Sample Input

3
Sample Output = 5 
i.e 

000
001
010
100
101
"""


def valid_binary_string_count(n) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 2  # 0 or 1 both valid
    return valid_binary_string_count(n - 1) + valid_binary_string_count(n - 2)


def all_valid_binary_strings(n) -> list[str]:
    result = []

    def helper(current_str, remaining):
        if remaining == 0:
            result.append(current_str)
            return

        helper(current_str + "0", remaining - 1)
        if not current_str or current_str[-1] != "1":
            helper(current_str + "1", remaining - 1)

    helper("", n)
    return result


if __name__ == "__main__":
    # print(valid_binary_string_count(0))
    # print(valid_binary_string_count(1))
    # print(valid_binary_string_count(2))
    # print(valid_binary_string_count(3))
    print(all_valid_binary_strings(3))
