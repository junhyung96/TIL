import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))


def binary_search():
    start = 0
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2
        # print(mid)
        if M <= get_tree_length(mid):
            start = mid + 1
        else:
            end = mid - 1

    return (start + end) // 2


def get_tree_length(height):
    sum_of_tree_length = 0

    for tree in trees:
        if tree > height:
            sum_of_tree_length += tree - height
    return sum_of_tree_length       


if M == 0:
    print(max(trees))
else:
    print(binary_search())