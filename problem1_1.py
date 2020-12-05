INPUT_FILE = 'data/problem1.txt'


def read_input():
    with open(INPUT_FILE, 'r') as input_file:
        return [int(line) for line in input_file]


def find_product(input_array):
    expected_sum = 2020
    left = 0
    right = len(input_array) - 1
    while left < right and input_array[left] + input_array[right] != expected_sum:
        if input_array[left] + input_array[right] > expected_sum:
            right -= 1
        else:
            left += 1
    if left == right:
        return 0
    return input_array[left] * input_array[right]


if __name__ == '__main__':
    print(find_product(sorted(read_input())))
