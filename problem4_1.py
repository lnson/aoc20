INPUT_FILE = 'data/problem4.txt'


class Passport:
    def __init__(self):
        self.fields = {}

    def is_valid(self):
        field_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        return (len(self.fields) == len(field_names) + int('cid' in self.fields) and
                all(map(lambda field_name: field_name in self.fields, field_names)))

    def add(self, key, value):
        self.fields[key] = value


def count_valid_passport_from_lines(lines):
    num_valid = 0
    current_passport = Passport()
    for line in lines:
        if line == '':
            num_valid += int(current_passport.is_valid())
            current_passport = Passport()
            continue
        for kv_pair_str in line.split():
            (key, value) = kv_pair_str.split(':')
            current_passport.add(key, value)

    num_valid += int(current_passport.is_valid())
    return num_valid


def count_valid_passports():
    with open(INPUT_FILE, 'r') as input_file:
        return count_valid_passport_from_lines(map(lambda line: line.rstrip('\n'), input_file))


if __name__ == '__main__':
    print(count_valid_passports())
