def is_valid(line):
    d = {}
    for entry in line.split(" "):
        if d.get(entry, False):
            return False
        else:
            d[entry] = 1
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
