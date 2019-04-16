class MinHeap:
    def __init__(self, n):
        self.seq = list()
        self.size = n
        self.result = list()

    def make_heap(self):
        [self.seq.append([i, 0]) for i in range(self.size)]

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left_child(index):
        return index * 2 + 1

    @staticmethod
    def right_child(index):
        return index * 2 + 2

    def swap(self, x, y):
        self.seq[x], self.seq[y] = self.seq[y], self.seq[x]

    def sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < self.size and self.seq[left][1] < self.seq[min_index][1]:
            min_index = left
        if right < self.size and self.seq[right][1] < self.seq[min_index][1]:
            min_index = right
        if left < self.size and self.seq[left][1] == self.seq[min_index][1] and \
                self.seq[left][0] < self.seq[min_index][0]:
            min_index = left
        if right < self.size and self.seq[right][1] == self.seq[min_index][1] and \
                self.seq[right][0] < self.seq[min_index][0]:
            min_index = right
        if min_index != i:
            self.swap(i, min_index)
            self.sift_down(min_index)

    def get_min(self):
        return self.seq[0]

    def change_priority(self, i, value):
        self.seq[i] = [self.seq[i][0], self.seq[i][1] + value]

    def add_process(self, task):
        self.result.append(self.get_min())
        if task == 0:
            pass
        else:
            self.change_priority(0, task)
            self.sift_down(0)


def main():
    n, m = map(int, input().split(" "))
    tasks = list(map(int, input().split()))
    h = MinHeap(n)
    h.make_heap()
    for task in tasks:
        h.add_process(task)
    for res in h.result:
        print(*res)


if __name__ == "__main__":
    main()
