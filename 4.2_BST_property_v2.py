import sys

sys.setrecursionlimit(100000)


class BinaryTree:
    def __init__(self, tree):
        self.tree = tree
        self.result = list()
        self.min = -2 ** 31
        self.max = 2 ** 31
        if len(tree) > 0:
            self.root = tree[0]["key"]

    def in_order(self, node, _min, _max):
        if node == -1:
            return
        if _min < self.tree[node]["key"] < _max:
            pass
        else:
            self.result.append("inc")
            return
        self.in_order(self.tree[node]["left"], _min, self.tree[node]["key"])
        self.in_order(self.tree[node]["right"], self.tree[node]["key"], _max)

    def implementation(self):
        if len(self.tree) == 0 or len(self.tree) == 1:
            return "CORRECT"
        self.in_order(self.tree[0]["left"], self.min, self.root)
        self.in_order(self.tree[0]["right"], self.root, self.max)
        if "inc" not in self.result:
            return "CORRECT"
        else:
            return "INCORRECT"


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
