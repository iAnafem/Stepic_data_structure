import sys

sys.setrecursionlimit(10000000)


class BinaryTree:
    def __init__(self, tree):
        self.tree = tree
        self.result = list()

    def in_order(self, node):
        if node == -1:
            return
        self.in_order(self.tree[node]["left"])
        self.result.append(self.tree[node]["key"])
        self.in_order(self.tree[node]["right"])
        return self.result

    def implementation(self):
        if len(self.tree) == 0 or len(self.tree) == 1:
            return "CORRECT"
        res = self.in_order(0)
        for i in range(len(res) - 1):
            if res[i] > res[i + 1]:
                return "INCORRECT"
        return "CORRECT"


def main():
    tree = list()
    n = (int(input()))
    for node in range(n):
        tree.append({"key": None, "left": None, "right": None})
        tree[node]["key"], tree[node]["left"], tree[node]["right"] = [int(i) for i in input().strip().split(" ")]
    t = BinaryTree(tree)
    print(t.implementation())


if __name__ == "__main__":
    main()
