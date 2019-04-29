class Hash:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.x = 263
        self.mod = 1000000007
        self.L = len(pattern)
        self.degree = self.L - 1
        self.pol = self.pow(self.degree)

    def pow(self, degree):
        if degree == 0:
            return 1
        elif degree == 1:
            return self.x
        elif degree % 2 == 0:
            result = self.pow(degree / 2)
            return (result * result) % self.mod
        else:
            return (self.pow(degree - 1) * self.x) % self.mod

    def pattern_hash(self):
        _hash = 0
        for i in range(len(self.pattern)):
            _hash += ((ord(self.pattern[i]) * self.pow(i)) % self.mod)
        return _hash % self.mod

    def right_hash(self, text):
        _hash = 0
        for i in range(len(text)):
            _hash += (ord(text[i]) * self.x ** i) % self.mod
        return _hash

    def recalculate(self, i, old_hash):
        return ord(self.text[i]) + ((old_hash - ord(self.text[i + self.L]) * self.pol) * self.x) % self.mod


def main():
    pattern = input().strip()
    text = input().strip()
    result = []
    h = Hash(pattern, text)
    pattern_hash = h.pattern_hash()
    start = len(text) - len(pattern)
    old_hash = h.right_hash(text[start:])
    if old_hash == pattern_hash:
        if text[start:] == pattern:
            result.insert(0, start)
    for i in range(start - 1, -1, -1):
        new_hash = h.recalculate(i, old_hash)
        if new_hash == pattern_hash:
            if text[i: i + h.L] == pattern:
                result.insert(0, i)
        old_hash = new_hash
    print(*result)


if __name__ == "__main__":
    main()





