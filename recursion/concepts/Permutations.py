"""
For all methods below time complexity is 2T(n-1) + 1 ==> O(2^n)
space = O(N)
"""

"""
input: ABC
ouput: ABC, A_BC, AB_C, A_B_C
"""

r"""

Input: "ABC"

                        "A""BC"
                       /     \
                    -B         B
                   /          /
              "A-B"         "AB"
              /    \        /    \
           -C        C   -C        C
           /          \   /          \
        "A-B-C"   "A-BC" "AB-C"     "ABC"
"""

"""
Recursive technique:
choice + decision

make input smaller each step, input-output method

"""

"""
ensure input is partitioned here before calling i.e output = s[0], input = s[1:]
"""


def permutation_with_spaces(output, input_str):
    if len(input_str) == 0:
        print(output)
        return

    permutation_with_spaces(output + "_" + input_str[0], input_str[1:])
    permutation_with_spaces(output + input_str[0], input_str[1:])
    return


"""
Input: ab
ouput: ab, aB, Ab, AB

everything same as above problem and assume input is in small case
"""

r"""
                              ("", "abc")
                            /             \
                ("a", "bc")                ("A", "bc")
                /          \              /            \
        ("ab", "c")    ("aB", "c")  ("Ab", "c")    ("AB", "c")
           /     \        /     \      /     \         /      \
    ("abc","") ("abC","") ("aBc","") ("aBC","") ("Abc","") ("AbC","") ("ABc","") ("ABC","")
        |          |          |          |          |          |          |          |
       abc        abC        aBc        aBC        Abc        AbC        ABc        ABC
"""


def permutation_with_case_change(output, input_str):
    if len(input_str) == 0:
        print(output)
        return

    permutation_with_case_change(output + input_str[0], input_str[1:])
    permutation_with_case_change(output + input_str[0].upper(), input_str[1:])
    return


r"""
                                    ("", "a1b2")
                                   /             \
                        ("a", "1b2")             ("A", "1b2")
                             |                        |
                        ("a1", "b2")             ("A1", "b2")
                         /        \               /        \
                ("a1b", "2")  ("a1B", "2")  ("A1b", "2")  ("A1B", "2")
                     |              |              |              |
                ("a1b2","")  ("a1B2","")   ("A1b2","")   ("A1B2","")
                     |              |              |              |
                   a1b2           a1B2           A1b2           A1B2
"""


# if all digits then time is O(N)
def letter_case_permutation(output, input_str):
    if len(input_str) == 0:
        print(output)
        return

    if input_str[0].isdigit():
        letter_case_permutation(output + input_str[0], input_str[1:])
    else:
        letter_case_permutation(output + input_str[0], input_str[1:])
        letter_case_permutation(output + input_str[0].upper(), input_str[1:])
        # if input is mix of small and upper alphabets then use .swapcase() instead of upper()
    return


if __name__ == "__main__":
    s = input("enter a string: ")
    # permutation_with_spaces(s[0], s[1:])
    # permutation_with_case_change("", s)
    print(letter_case_permutation("", s))
