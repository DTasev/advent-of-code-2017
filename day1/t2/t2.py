from typing import List


def process(chars):
    sum = 0
    chars_len = len(chars)
    step = chars_len // 2
    for i in range(-1, chars_len - 1):
        if chars[i] == chars[(i + step) % chars_len]:
            sum += int(chars[i])
    print(sum)
    print("next number\n")


def main():
    data = List[str]
    with open('test.txt', 'r') as f:
        data = f.readlines()

    for i in data:
        # remove new charss
        i = i.strip()
        process(i)


main()
