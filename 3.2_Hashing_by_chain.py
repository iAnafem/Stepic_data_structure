class ChainHash:
    def __init__(self, _hash):
        self.hash = _hash
        self.x = 263
        self.mod = 1000000007
        self.output = list()

    def pow(self, degree):
        result = self.x
        for i in range(degree - 1):
            result *= self.x % self.mod
        return result

    def calc_hash(self, string):
        result = ord(string[0])
        for i in range(1, len(string)):
            result += ord(string[i]) * self.pow(i)
        result = (result % self.mod) % len(string)
        return result

    def add_string(self, string):
        pass

    def del_string(self, string):
        pass

    def find_string(self, string):
        pass

    def check_string(self, i):
        pass


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
            c.find_string(req[1])
        else:
            c.check_string(req[1])
    print(c.calc_hash("world"))
    print(c.calc_hash("lol"))
    print(c.calc_hash("HellO"))
    print(c.calc_hash("pursue"))
    print(c.calc_hash("WORLD"))
    print(c.calc_hash("Haskel"))
    return c


def tests(c):
    assert c.calc_hash("world") == 4
    assert c.calc_hash("HellO") == 4


if __name__ == "__main__":
    tests(main())




