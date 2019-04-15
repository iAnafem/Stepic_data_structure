class MinHeap:
    def __init__(self, seq, processors):
        self.seq = seq
        self.result = list()
        self.size = len(seq)
        self.max_size = processors

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
        left = self.left_child(i)
        right = self.right_child(i)
        if left < self.size and self.seq[i][1] == self.seq[left][1] and self.seq[i][0] > self.seq[left][0]:
            self.swap(i, left)
        elif right < self.size and self.seq[i][1] == self.seq[right][1] and self.seq[i][0] > self.seq[right][0]:
            self.swap(i, right)

    def sift_up(self, i):
        while i > 0 and self.seq[self.parent(i)][1] > self.seq[i][1]:
            print(self.parent(i), i)
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
        self.check_processors(min_index)

    def get_min(self):
        return self.seq[0][1]

    def insert(self, task):
        self.seq.append([len(self.seq), task])

    def change_priority(self, i, value):
        self.seq[i][1] = self.seq[i][1] + value

    def add_process(self, task):
        if len(self.seq) >= self.max_size:
            self.result.append(self.seq[0])
            self.change_priority(0, task)
            self.sift_down(0)
        else:
            self.insert(task)
            if len(self.seq) > 1:
                self.sift_up(len(self.seq))
            self.result.append(self.seq[0])


def main():
    n, m = map(int, input().split(" "))
    tasks = list(map(int, input().split()))
    heap = list()
    h = MinHeap(heap, n)
    for task in tasks:
        h.add_process(task)
        print(h.seq)

    print(h.result)

    print(h.seq)
#    print(len(h.result))
#    for pair in h.result:
 #       print(*pair)


if __name__ == "__main__":
    main()
