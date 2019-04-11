class MinHeap:
    def __init__(self, seq):
        self.seq = seq
        self.result = list()
        self.size = len(seq)

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
        if left < self.size and self.seq[left] < self.seq[min_index]:
            min_index = left
        if right < self.size and self.seq[right] < self.seq[min_index]:
            min_index = right
        if min_index != i:
            self.result.append([i, min_index])
            self.swap(i, min_index)
            self.sift_down(min_index)


def main():
    n = int(input().strip())
    _seq = list(map(int, input().split()))
    h = MinHeap(_seq)
    for item in range(n // 2 - 1, -1, -1):
        h.sift_down(item)
    print(len(h.result))
    for pair in h.result:
        print(*pair)


if __name__ == "__main__":
    main()
