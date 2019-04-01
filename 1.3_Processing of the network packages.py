class Package:
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration


class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = list()
        self.process = 0

    def check(self, pack):
        if len(self.buffer) < self.size:
            return True
        else:
            if pack.arrival >= self.buffer[0][1]:
                self.buffer.remove(self.buffer[0])
            if len(self.buffer) < self.size:
                return True
            else:
                return False

    def push(self, pack):
        start = max(self.process, pack.arrival)
        end = start + pack.duration
        print(start)
        self.buffer.append((start, end))
        self.process = end

    def add_package(self, pack):
        if self.check(pack):
            self.push(pack)
        else:
            print(-1)


def main():
    _size, n = map(int, input().split(" "))
    lst = [Package(*map(int, input().split())) for i in range(n)]
    print(lst)
    buffer = Buffer(_size)
    for p in lst:
        buffer.add_package(p)


if __name__ == "__main__":
    main()
