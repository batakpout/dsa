# Also called Print PowerSets | Print all Subsequences

def subsets(output, input):
    if len(input) == 0:
        print(output, end=" ")
        return
    op1 = output
    op2 = output  # direct op2 += input[0] not allowed by python, have to create it here first

    op2 += input[0]
    input = input[:1]
    subsets(op1, input)
    subsets(op2, input)
    return  # not needed


def concise_version(output, input_str):
    if len(input_str) == 0:
        print(output)
        return

    concise_version(output, input_str[1:])
    concise_version(output + input_str[0], input_str[1:])
    return


if __name__ == "__main__":
    concise_version("", "ab")
    print("*" * 30)
    concise_version("", "abc")
    print("*" * 30)
    concise_version("", "abcd")
