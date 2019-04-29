class Hash:
    def __init__(self):
        self.x = 263
        self.mod = 1000000007
        self.result = list()

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

    def calc_hash(self, string):
        _hash = 0
        for i in range(len(string)):
            _hash += ((ord(string[i]) * self.pow(i)) % self.mod)
        return _hash % self.mod

    def rolling_hash(self, prev_hash, left, right, pow_right):
        return ((prev_hash - (right * pow_right) % self.mod) * self.x + left) % self.mod

    def implementation(self, pattern, text):
        self.result.clear()
        size = len(pattern)
        if pattern == text:
            return [0]
        pattern_hash = self.calc_hash(pattern)
        window_hash = self.calc_hash(text[-size:])
        pow_right = self.pow(size - 1)
        i = len(text) - size
        while True:
            if window_hash == pattern_hash and text[i] == pattern[0] and text[i + size - 1] == pattern[-1]:
                self.result += [i]
            i -= 1
            if i < 0:
                break
            window_hash = self.rolling_hash(window_hash, ord(text[i]), ord(text[i + size]), pow_right)
        return self.result


def main():
    h = Hash()
    print(*reversed(h.implementation(input().strip(), input().strip())))


def tests():
    h_test = Hash()
    assert h_test.implementation("aba", "abacaba") == [4, 0]
    assert h_test.implementation("Test", "testTesttesT") == [4]
    assert h_test.implementation("aaaaa", "baaaaaaa") == [3, 2, 1]
    assert h_test.implementation("aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa") == [0]


if __name__ == "__main__":
    tests()
    main()
