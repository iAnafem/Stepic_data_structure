def height(_tree):
    res = {}
    for i, n in enumerate(tree):
        h = 1
        while n != -1:
            h += 1
            n = tree[n]
            calc_height = res.get(n, 0)
            if calc_height:
                h += calc_height
                break

        res[i] = h
        yield h


num = int(input())
tree = list(map(int, input().split()))
print(max(height(tree)))

