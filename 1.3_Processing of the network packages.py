class Package:
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration


class Buffer:
    def __init__(self, size):
        self.size = size
        self.log = list()
        self.buffer = list()

    def check(self, pack):
        if len(self.buffer) < self.size:
            return True
        else:
            for i in self.buffer:
                if pack.arrival >= i[1]:
                    self.buffer.pop(i)
            if len(self.buffer) < self.size:
                return True
            else:
                return False

    def push(self, pack):
        self.buffer.append([pack.arrival, pack.duration])

    def add_package(self, pack):
        if self.check(pack):
            self.push(pack)


