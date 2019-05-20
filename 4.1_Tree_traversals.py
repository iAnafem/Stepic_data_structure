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

    def pre_order(self, node):
        if node == -1:
            return
        self.result.append(self.tree[node]["key"])
        self.pre_order(self.tree[node]["left"])
        self.pre_order(self.tree[node]["right"])
        return self.result

    def post_order(self, node):
        if node == -1:
            return
        self.post_order(self.tree[node]["left"])
        self.post_order(self.tree[node]["right"])
        self.result.append(self.tree[node]["key"])
        return self.result

    def implementation(self):
        print(*self.in_order(0))
        self.result.clear()
        print(*self.pre_order(0))
        self.result.clear()
        print(*self.post_order(0))


def main():
    tree = list()
    n = (int(input()))
    for node in range(n):
        tree.append({"key": None, "left": None, "right": None})
        tree[node]["key"], tree[node]["left"], tree[node]["right"] = [int(i) for i in input().strip().split(" ")]
    t = BinaryTree(tree)
    t.implementation()


if __name__ == "__main__":
    main()
