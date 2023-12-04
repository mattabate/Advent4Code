def letter_value(full_string, i):
    cut = full_string[i:]
    if cut.startswith("one") or cut.startswith("1"):
        return 1
    elif cut.startswith("two") or cut.startswith("2"):
        return 2
    elif cut.startswith("three") or cut.startswith("3"):
        return 3
    elif cut.startswith("four") or cut.startswith("4"):
        return 4
    elif cut.startswith("five") or cut.startswith("5"):
        return 5
    elif cut.startswith("six") or cut.startswith("6"):
        return 6
    elif cut.startswith("seven") or cut.startswith("7"):
        return 7
    elif cut.startswith("eight") or cut.startswith("8"):
        return 8
    elif cut.startswith("nine") or cut.startswith("9"):
        return 9
    else:
        return None


def compute_score(test):
    lines = test.strip().strip().split("\n")

    total = 0
    for line in lines:
        first = None
        last = None
        for l in line:
            if l.isdigit():
                if not first:
                    first = l
                last = l

        if not first or not last:
            print("errror")
            return None
        num = first + last
        total += int(num)

    return total


def compute_score_part_2(test):
    lines = test.strip().strip().split("\n")

    total = 0
    for line in lines:
        first = None
        last = None
        for i, l in enumerate(line):
            out = letter_value(line, i)
            if out:
                if not first:
                    first = str(out)
                last = str(out)

        if not first or not last:
            print("errror")
            return None
        num = first + last
        total += int(num)

    return total


if __name__ == "__main__":
    test = False

    with open("supplimental.txt", "r") as f:
        text = f.read()

    if test:
        text = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
        scrore = compute_score(text)
        print("PART 1:", scrore)

        text = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
        scrore = compute_score_part_2(text)
        print("PART 2:", scrore)
        exit()

    scrore = compute_score(text)
    print("PART 1:", scrore)
    scrore = compute_score_part_2(text)
    print("PART 2:", scrore)
