class Package:
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration
        self.end = self.arrival + self.duration


class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = list()
        self.process = 0
        self.log = []

    def check(self, pack):
        if len(self.buffer) < self.size:
            return True
        else:
            if pack.end == 0:
                return True
            for i in self.buffer:
                if pack.arrival >= i.end:
                    self.buffer.remove(i)
            if len(self.buffer) < self.size:
                return True
            else:
                return False

    def push(self, start, end):
        self.buffer.append(end)
        self.log.append(start)

    def add_package(self, pack):
        if self.check(pack):
            if len(self.buffer) == 0:
                self.push(pack.end)
                self.process += pack.end
                return pack.arrival
            else:
                self.push(pack)
                return pack.arrival + self.buffer[0].duration
        else:
            return -1


def main():
    _size, n = map(int, input().split(" "))
    lst = [Package(*map(int, input().split())) for i in range(n)]
    buffer = Buffer(_size)
    for p in lst:

        print(buffer.add_package(p))
        print(buffer.process)


if __name__ == "__main__":
    main()

"""
class Package:
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration
        self.end = self.arrival + self.duration


class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = list()
        self.process = 0
    
    def check(self, pack):
        if len(self.buffer) < self.size:
            return True
        else:
            if pack.end == 0:
                return True
            for i in self.buffer:
                if pack.arrival >= i.end:
                    self.buffer.remove(i)
            if len(self.buffer) < self.size:
                return True
            else:
                return False

    def push(self, pack):
        self.buffer.append(pack)

    def add_package(self, pack):
        if self.check(pack):
            if len(self.buffer) == 0:
                self.push(pack)
                return pack.arrival
            else:
                self.push(pack)
                return pack.arrival + self.buffer[0].duration
        else:
            return -1


def main():
    _size, n = map(int, input().split(" "))
    lst = [Package(*map(int, input().split())) for i in range(n)]
    buffer = Buffer(_size)
    for p in lst:
        
        print(buffer.add_package(p))
        


if __name__ == "__main__":
    main()
"""