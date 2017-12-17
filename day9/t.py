def preprocess(inp):
    brackets = []
    naive_chars = 0
    reading_garbage = False
    ignore_once = False
    for c in inp:
        if ignore_once:
            ignore_once = False
            continue

        if c == '!':
            ignore_once = True
            continue

        if reading_garbage:
            if c == '>':
                reading_garbage = False
                continue
            naive_chars += 1
            continue

        if c == '{' or c == '}':  # legit bracket
            brackets.append(c)
        elif c == '<':  # garbage start
            reading_garbage = True

    return brackets, naive_chars


def calculate(inp):
    score = 0

    stack = []
    for c in inp:
        if c == '{':
            stack.append(c)
        else:
            score += len(stack)
            stack.pop()

    return score


def test():
    data = [
        ("{}", 1),
        ("{{{}}}", 6),  # score of 1 + 2 + 3
        ("{{},{}}", 5),  # score of 1 + 2 + 2
        ("{{{},{},{{}}}}", 16),  # score of 1 + 2 + 3 + 3 + 3 + 4
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),  # score of 1 + 2 + 2 + 2 + 2
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),  # score of 1 + 2 + 2 + 2 + 2
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)
    ]  # score of 1 + 2

    for d in data:
        brackets, chars = preprocess(d[0])
        result = calculate(brackets)
        print("Expected: {}, Actual: {}".format(d[1], result))


def run():
    with open('input.txt', 'r') as f:
        data = f.readlines()[0].strip()

    brackets, chars = preprocess(data)
    res = calculate(brackets)
    print("Bracket score:", res)
    print("Length of garbage chars:", chars)


test()

run()
