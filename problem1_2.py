INPUT_FILE = 'data/problem1.txt'

def read_input():
    with open(INPUT_FILE, 'r') as input_file:
        return [int(line) for line in input_file]


def make_index_map(input_array):
    index_map = {}
    for i in range(len(input_array)):
        if i in index_map:
            index_map[input_array[i]].add(i)
        else:
            index_map[input_array[i]] = {i}
    return index_map


def find_3_product(input_array):
    index_map = make_index_map(input_array)
    expected_sum = 2020
    for i in range(len(input_array)):
        for j in range(i, len(input_array)):
            x = expected_sum - (input_array[i] + input_array[j])
            if x not in index_map:
                continue
            indices_of_x = index_map[x]
            num_used_indices = int(i in indices_of_x) + int(j in indices_of_x)
            if len(indices_of_x) > num_used_indices:
                return input_array[i] * input_array[j] * x

    return 0


if __name__ == '__main__':
    print(find_3_product(read_input()))
