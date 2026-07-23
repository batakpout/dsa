# Also called Print PowerSets | Print all Subsequences

"""
Used input output method i.e make input small and make a recursive tree
"""

"""
General rule: abc
subsets : '', a, b, c, ab, ac, bc, abc. Here ac can be written as ca but this is not allowed in subsequence
substring: contagious i.e a, b, c, ab, bc, abc , but not ac
subsequence: a, b, c, ab, bc, abc, ac,  but not ca

So if we asked to print subsequences in question, subset only we can print, the way we did below
but, printing sub-strings could be a different question
"""

"""
All Subsets
input : ab
output: '', a, b, ab and {'','a', 'b', 'ab'} ==> powerset: set of all subsets
so print subsets and print powerset is one and the same thing. Also print subsequences is also same.
2^3 = 8 subsets.
"""
def all_subsets(output, input):
    if len(input) == 0:
        print(output, end=" ")
        return
    op1 = output
    op2 = output  # direct op2 += input[0] not allowed by python, have to create it here first

    op2 += input[0]
    input = input[:1]
    all_subsets(op1, input)
    all_subsets(op2, input)
    return  # not needed


def concise_version_all_subsets(output, input_str):
    if len(input_str) == 0:
        print(output)
        return

    concise_version_all_subsets(output, input_str[1:])
    concise_version_all_subsets(output + input_str[0], input_str[1:])
    return


"""
input: aab
output: {'', 'a', 'a', 'b', 'aab', 'aa', 'ab', 'ab'}
unique output: {'', 'a', 'b', 'aab', 'aa', 'ab'}
"""


def unique_concise_version_all_subsets(input_str) -> set[int]:
    seen = set()

    def helper(output, input_str):
        if len(input_str) == 0:
            seen.add(output)
            return

        helper(output, input_str[1:])
        helper(output + input_str[0], input_str[1:])

    helper("", input_str)
    return seen


if __name__ == "__main__":
    concise_version_all_subsets("", "aab")
    print("*" * 30)
    # concise_version("", "abc")
    print("*" * 30)
    # concise_version("", "abcd")
    print(unique_concise_version_all_subsets("aab"))
