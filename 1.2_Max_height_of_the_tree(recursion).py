import sys

sys.setrecursionlimit(20000)


def height(root):
    h = 1
    if root not in res:
        return h
    for child in res[root]:
        h = max(h, 1 + height(child))
    return h


num = int(input())
tree = list(map(int, input().split()))
res = {}
for i in range(len(tree)):
    if tree[i] not in res:
        res[tree[i]] = [i]
    else:
        res[tree[i]] += [i]

print(height(res[-1][0]))
