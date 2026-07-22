def print_spell(num):
    spell = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def loop(n):
        if n <= 0:
            return
        last_digit = n % 10
        loop(n // 10)
        print(spell[last_digit])

    loop(num)


if __name__ == "__main__":
    num1 = 2021
    print_spell(num1)
