def height(_tree):
    for i, n in enumerate(tree):
        h = 1
        while n != -1:
            h += 1
            n = tree[n]
        yield h


num = int(input())
tree = list(map(int, input().split()))
print(max(height(tree)))


