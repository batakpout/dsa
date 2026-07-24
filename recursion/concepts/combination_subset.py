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
"""
def permutation(output, input_str):
    if len(input_str) == 0:
        print(output)
        return

    permutation(output + "_" + input_str[0], input_str[1:])
    permutation(output + input_str[0], input_str[1:])
    return


if __name__ == "__main__":

    s = input("enter a string: ")
    permutation(s[0], s[1:])
