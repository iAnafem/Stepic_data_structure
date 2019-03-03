def height(_tree):
    res = {}
    for i, n in enumerate(tree):
        h = 1
        print("входная n = ", n)
        while n != -1:
            print("цикловая n = ", n)
            h += 1
            n = tree[n]
            calc_height = res.get(n, 0)
            if calc_height:
                print("do that  ", calc_height)
                h += calc_height
                print(h)
                break

        res[i] = h
        print(res)
        yield h


num = int(input())
tree = list(map(int, input().split()))
print(max(height(tree)))

