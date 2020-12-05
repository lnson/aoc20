INPUT_FILE = 'data/problem2.txt'


def main():
    result = 0
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            (indices, c, s) = line.split(' ', 3)
            c = c[0:-1]  # remove the colon.
            result += int(sum(map(lambda idx: int(idx <= len(s) and s[idx - 1] == c),
                                  map(int, indices.split('-')))) == 1)
    print(result)


if __name__ == "__main__":
    main()
