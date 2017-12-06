from collections import Counter


def is_valid(line):
    history = []
    for entry in line.split(" "):
        current = Counter(entry)
        for previous in history:
            if previous == current:
                return False
        history.append(current)
    return True


def main():
    with open('input.txt', 'r') as f:
        data = [d.strip() for d in f.readlines()]
    answers = []
    for line in data:
        answers.append(is_valid(line))

    print("True:", answers.count(True))
    print("False:", answers.count(False))


main()
