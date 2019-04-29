class PhoneBook:
    def __init__(self):
        self._dict = dict()

    def add_contact(self, number, name):
        self._dict[number] = name

    def del_contact(self, number):
        if number in self._dict:
            self._dict.pop(number)
        else:
            return

    def find_contact(self, number):
        if number in self._dict:
            return self._dict[number]
        else:
            return "not found"


def main():
    n = int(input().strip())
    numbers = [[*map(str, input().strip().split(" "))] for i in range(n)]
    pb = PhoneBook()
    for num in numbers:
        if num[0] == "add":
            pb.add_contact(num[1], num[2])
        elif num[0] == "del":
            pb.del_contact(num[1])
        else:
            print(pb.find_contact(num[1]))


if __name__ == "__main__":
    main()
