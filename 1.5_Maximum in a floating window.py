class QueueMod:
    def __init__(self, lst, win):
        self.lst = lst
        self.win = win
        self._in = list()
        self._out = list()
        self.result = list()

    def pop_item(self):
        if self._out:
            self._out.pop()
        else:
            for i in range(self.win - 1, -1, -1):
                if len(self._out) == 0 or self._in[i][0] > self._out[-1][1]:
                    self._out.append([self._in[i][0], self._in[i][0]])
                elif self._in[i][0] <= self._out[-1][1]:
                    self._out.append([self._in[i][0], self._out[-1][1]])
            self._in.clear()
            self._out.pop()

    def add_item(self, _item):
        self.pop_item()
        if len(self._in) == 0 or _item > self._in[-1][1]:
            self._in.append([_item, _item])
        else:
            self._in.append([_item, self._in[-1][1]])

    def comparison(self):
        if len(self._out) == 0:
            self.result.append(self._in[-1][1])
        elif self._in[-1][1] <= self._out[-1][1]:
            self.result.append(self._out[-1][1])
        elif self._in[-1][1] > self._out[-1][1]:
            self.result.append(self._in[-1][1])

    def create_queue(self):
        self._in.append([self.lst[0], self.lst[0]])
        for item, i in zip(self.lst[1:self.win], range(self.win)):
            if self._in is False or item > self._in[i][1]:
                self._in.append([item, item])
            else:
                self._in.append([item, self._in[i][1]])


def main():
    n = int(input())
    seq = tuple(map(int, input().split(" ")))
    window = int(input())
    q = QueueMod(seq, window)
    q.create_queue()
    q.comparison()
    for i in seq[window:]:
        q.add_item(i)
        q.comparison()
    print(*q.result)


if __name__ == "__main__":
    main()
