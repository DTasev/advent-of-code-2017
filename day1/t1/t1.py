from typing import List


def process(chars):
    sum = 0
    for i in range(-1, len(chars) - 1):
        if chars[i] == chars[i + 1]:
            sum += int(chars[i])
    print(sum)
    print("next number\n")


def main():
    data = List[str]
    with open('input.txt', 'r') as f:
        data = f.readlines()

    for i in data:
        # remove new charss
        i = i.strip()
        process(i)


main()
