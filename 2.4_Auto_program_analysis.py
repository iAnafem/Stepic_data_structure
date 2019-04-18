class DSU:
    """ disjoint-set-union class"""
    def __init__(self, parent):
        self.parent = parent

    def find_set(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union_set(self, dest, source):
        _dest = self.find_set(dest)
        _source = self.find_set(source)
        if _dest != _source:
            self.parent[_source] = _dest
        return self.parent[_source]


def main():
    n, e, d = map(int, input().split(" "))
    equality = [[*map(int, input().split())] for i in range(e)]
    comparison = [[*map(int, input().split())] for i in range(d)]
    dsu = DSU(list(i for i in range(n + 1)))
    for eq in equality:
        dsu.union_set(eq[0], eq[1])
    for com in comparison:
        if dsu.find_set(com[0]) == dsu.find_set(com[1]):
            print(0)
            exit()
    print(1)


if __name__ == "__main__":
    main()
