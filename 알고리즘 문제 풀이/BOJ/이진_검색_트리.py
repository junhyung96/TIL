import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

tree_dict = {}
arr = []
i = 0

def make_tree(node, index):
    pass

# 입력 받으면서 이진트리에 값 저장하기
while True:
    try:
        num = int(input())
        if i == 0:
            i += 1
            tree_dict[i] = num
        else:
            if num > tree_dict[i]:
                while num > tree_dict[i]:
                    if i == 1:
                        break
                    if num > tree_dict[i//2]:
                        i //= 2
                    else:
                        break
                while tree_dict.get(i):
                    i = 2 * i + 1
                tree_dict[i] = num
            else:
                i *= 2
                tree_dict[i] = num
    except:
        break

def post_order(node):
    if not tree_dict.get(node):
        return
    post_order(node*2)
    post_order(node*2+1)
    print(tree_dict[node])

post_order(1)
# print(tree_dict)