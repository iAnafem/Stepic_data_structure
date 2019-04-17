class DSU:
    """ disjoint-set-union class"""
    def __init__(self, tables):
        self.tables = tables

    def find_set(self, x):
        if self.tables[x][0] == - 1:
            x = self.tables[x][1]
            return self.find_set(x)
        else:
            self.tables[x][1] = x
            return x

    def union_set(self, dest, source):
        if dest == source or self.tables[dest][1] == self.tables[source][1]:
            return self.tables[0]
        _dest = self.find_set(dest)
        _source = self.find_set(source)
        self.tables[_dest][0] += self.tables[_source][0]
        self.tables[_source][0], self.tables[_source][1] = - 1, _dest
        if self.tables[_dest][0] > self.tables[0]:
            self.tables[0] = self.tables[_dest][0]
        return self.tables[0]


def main():
    n, m = map(int, input().split(" "))
    strings = list(map(int, input().split()))
    merges = [[*map(int, input().split())] for i in range(m)]
    tables = list([_str, parent] for _str, parent in zip(strings, range(1, n + 1)))
    tables.insert(0, max(strings))
    dsu = DSU(tables)
    result = list()
    for merge in merges:
        result.append(dsu.union_set(merge[0], merge[1]))
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
