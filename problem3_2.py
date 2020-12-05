INPUT_FILE = 'data/problem3.txt'


def read_map():
    with open(INPUT_FILE, 'r') as input_file:
        return [line.rstrip('\n') for line in input_file]


def is_tree(c):
    return c == '#'


def count_tree(area, row_delta, col_delta):
    row, col = 0, 0
    num_tree = 0
    while row < len(area):
        num_tree += int(is_tree(area[row][col % len(area[row])]))
        row, col = row + row_delta, col + col_delta
    return num_tree


if __name__ == '__main__':
    my_map = read_map()
    print(count_tree(my_map, 1, 1) * count_tree(my_map, 1, 3) *
          count_tree(my_map, 1, 5) * count_tree(my_map, 1, 7) *
          count_tree(my_map, 2, 1))
