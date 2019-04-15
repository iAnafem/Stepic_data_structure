class MinHeap:
    def __init__(self, seq, n):
        self.seq = seq
        self.result = list()
        self.size = n

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

    def check_processors(self, i):
        print("do check")
        left = self.left_child(i)
        right = self.right_child(i)
        if left < self.size and self.seq[i][1] == self.seq[left][1] and self.seq[i][0] > self.seq[left][0]:
            self.swap(i, left)
        elif right < self.size and self.seq[i][1] == self.seq[right][1] and self.seq[i][0] > self.seq[right][0]:
            self.swap(i, right)

    def sift_up(self, i):
        while i > 0 and self.seq[self.parent(i)][1] > self.seq[i][1]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < self.size and self.seq[left][1] < self.seq[min_index][1]:
            min_index = left
        if right < self.size and self.seq[right][1] < self.seq[min_index][1]:
            min_index = right
        if min_index != i:
            self.swap(i, min_index)
            self.sift_down(min_index)
        #self.check_processors(min_index)
        print(self.seq)

    def get_min(self):
        return self.seq[0][1]

    def insert(self, task):
        self.seq.append([len(self.seq), task])

    def change_priority(self, i, value):
        self.seq[i][1] = self.seq[i][1] + value
        self.sift_down(i)

    def add_process(self, task):
        self.result.append(self.seq[0])
        self.change_priority(0, task)


def main():
    n, m = map(int, input().split(" "))
    tasks = list(map(int, input().split()))
    heap = list([i, 0] for i in range(n))
    h = MinHeap(heap, n)
    for item in heap:
        h.result.append(item)
    for task in tasks:
        print("do next")
        h.add_process(task)
    for res in h.result:
        print(*res)


if __name__ == "__main__":
    main()
