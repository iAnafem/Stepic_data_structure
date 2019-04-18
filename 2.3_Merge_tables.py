class DSU:
    """ disjoint-set-union class"""
    def __init__(self, tables, _max):
        self.tables = tables
        self.parent = list(i for i in range(len(self.tables)))
        self._max = _max
        self.result = list()

    def find_set(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union_set(self, dest, source):
        _dest = self.find_set(dest)
        _source = self.find_set(source)
        if _dest != _source:
            self.parent[_source] = _dest
            self.tables[_dest] += self.tables[_source]
            if self._max < self.tables[_dest]:
                self._max = self.tables[_dest]
        self.result.append(self._max)
        return self.parent[_source]


def main():
    n, m = map(int, input().split(" "))
    tables = list(map(int, input().split()))
    merges = [[*map(int, input().split())] for i in range(m)]
    _max = max(tables)
    tables.insert(0, _max)
    dsu = DSU(tables, _max)
    for merge in merges:
        dsu.union_set(merge[0], merge[1])
    for res in dsu.result:
        print(res)


if __name__ == "__main__":
    main()
