"""
Time-Complexity:-

How many recursive calls?
At each level:
Level 0: (n) choices e.g n = 4
Level 1: (n-1) choices , total:- n*(n-1), 4 * 3 = 12
Level 2: (n-2) choices, total :- n*(n-1)(n-2), 4*3*2 = 24
...
at last: 1 choice , 4*3*2*1 = 24
So the number of leaves is:-
4+12+24+24 = 24 we took dominating term, so 24 i.e n!

Time complexity = work done per node * total nodes

work done per node = string ops so O(N) [The for loop is already represented within the recursion tree, so we don't need
 to factor it separately into the complexity]

 Therefore, the overall complexity is O(n × n!), not O(n² × n!)]

 Space complexity: O(n * n!) [result list] , n! is total strings with each of size n, this is dominating factor
 we ignore small ones e.g O(N) recursive stack, temporary strings formed 
"""

def using_recursion(s: str) -> list[str]:
    result = []

    def helper(input, output):
        if not input:
            result.append(output)
            return
        seen = set()
        for i, ch in enumerate(input):
            if ch in seen:
                continue

            seen.add(ch)
            helper(input[:i] + input[i + 1:], output + ch)

    helper(s, "")
    return result


if __name__ == "__main__":
    input = input("enter a string:-")
    print(using_recursion(input))
