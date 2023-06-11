# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7

def parse_input():
    num_testcase = int(input())
    test_sets = []
    for _ in range(num_testcase):
        n, k, s = input().split(" ")
        n, k, s = int(n), int(k), int(s)
        test_sets.append([n, k, s])
    return test_sets


def solve(total, current, sord):
    minutes = current - 1
    diff = current - sord
    if diff*2 > current:
        minutes += (total + 1)
    else:
        minutes += (diff*2 + total - current + 1)
    return minutes


for i, test_set in enumerate(parse_input()):
    print("Case #{}: {}".format(
        i+1, solve(test_set[0], test_set[1], test_set[2])))
