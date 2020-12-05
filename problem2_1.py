INPUT_FILE = 'data/problem2.txt'


def main():
    result = 0
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            (occ, c, s) = line.split(' ', 3)
            (min_occ, max_occ) = map(int, occ.split('-'))
            c = c[0:-1]  # remove the colon.
            result += int(min_occ <= s.count(c) <= max_occ)
    print(result)


if __name__ == "__main__":
    main()
