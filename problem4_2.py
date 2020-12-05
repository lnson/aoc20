import re


INPUT_FILE = 'data/problem4.txt'


def valid_year(s, low, high):
    return re.search("^[0-9]{4}$", s) and low <= int(s) <= high


def valid_height(s):
    m = re.search("^([0-9]+)(cm|in)$", s)
    if not m:
        return False
    if m.group(2) == "cm":
        return 150 <= int(m.group(1)) <= 193
    return 59 <= int(m.group(1)) <= 76


def valid_html_color(s):
    return re.search("^#[0-9a-f]{6}$", s)


class Passport:
    def __init__(self):
        self.fields = {}

    def is_valid(self):
        field_validators = {'byr': lambda s: valid_year(s, 1920, 2002),
                            'iyr': lambda s: valid_year(s, 2010, 2020),
                            'eyr': lambda s: valid_year(s, 2020, 2030),
                            'hgt': valid_height,
                            'hcl': valid_html_color,
                            'ecl': lambda s: s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
                            'pid': lambda s: re.search("^[0-9]{9}$", s)}
        for (field_name, validator) in field_validators.items():
            if field_name not in self.fields or not validator(self.fields[field_name]):
                return False
        return len(self.fields) == len(field_validators) + int('cid' in self.fields)

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
