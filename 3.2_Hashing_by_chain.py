class ChainHash:
    def __init__(self, _dict):
        self._dict = _dict
        self.x = 263
        self.mod = 1000000007

    def pow(self, degree):
        if degree == 0:
            return 1
        elif degree == 1:
            return self.x
        elif degree % 2 == 0:
            result = self.pow(degree / 2)
            return (result * result) % self.mod
        else:
            return (self.pow(degree - 1) * self.x) % self.mod

    def calc_hash(self, string):
        _hash = 0
        for i in range(len(string)):
            _hash += ((ord(string[i]) * self.pow(i)) % self.mod)
        return _hash % self.mod % len(self._dict)

    def add_string(self, string):
        if self.find_string(string) == "yes":
            return
        else:
            self._dict[self.calc_hash(string)].insert(0, string)

    def del_string(self, string):
        if self.find_string(string) == "yes":
            self._dict[self.calc_hash(string)].remove(string)

    def find_string(self, string):
        if string in self._dict[self.calc_hash(string)]:
            return "yes"
        else:
            return "no"

    def check_string(self, i):
        print(*self._dict[i])


def main():
    m = int(input().strip())
    n = int(input().strip())
    requests = [[*map(str, input().strip().split(" "))] for i in range(n)]
    c = ChainHash({i: [] for i in range(m)})
    for req in requests:
        if req[0] == "add":
            c.add_string(req[1])
        elif req[0] == "del":
            c.del_string(req[1])
        elif req[0] == "find":
            print(c.find_string(req[1]))
        else:
            c.check_string(int(req[1]))

    return c


def tests(c):
    assert c.calc_hash("GooD") == 2
    assert c.calc_hash("luck") == 2
    assert c.calc_hash("world") == 4
    assert c.calc_hash("HellO") == 4


if __name__ == "__main__":
    tests(main())




