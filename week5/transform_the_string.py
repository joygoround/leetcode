# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461


def parse_input():
    num_testcase = int(input())
    test_sets = []
    for _ in range(num_testcase):
        s = input()
        f = input()
        test_sets.append([s, f])
    return test_sets


def calculate_distance(char, alpa):
    diff = abs(ord(char)-ord(alpa))
    return diff if diff <= 13 else 26 - diff


def solve(s, f):
    op_count = 0
    bag_of_char = list(f)
    for char in list(s):
        if char not in bag_of_char:
            op_count += min([calculate_distance(char, alpa)
                             for alpa in bag_of_char])
    return op_count


for i, test_set in enumerate(parse_input()):
    print("Case #{}: {}".format(i+1, solve(test_set[0], test_set[1])))
