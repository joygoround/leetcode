#  https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32

def parse_input():
    num_testcase = int(input())
    test_sets = [[int(input()), list(input())] for _ in range(num_testcase)]
    return test_sets


def solve(test_set):
    n, houses = test_set
    sum_distance = 0
    count_bins = houses.count("1")
    low = houses.index("1")
    high = houses.index("1", count_bins-1)
    for i in range(n):
        if houses[i] == "1":
            low = i
            count_bins -= 1
            if count_bins > 0:
                high = houses.index("1", i+1)
        else:
            sum_distance += min(abs(i-low), abs(high-i))

    return sum_distance


for i, test_set in enumerate(parse_input()):
    print("Case #{}: {}".format(i+1, solve(test_set)))
