def find_max(_lst, _win):
    stack = _lst[:_win]
    max_stack = [0]
    [max_stack.append(num) for num in stack if num > max_stack[-1]]
    print(max_stack[-1], end=" ")
    max_stack.pop(0)


def main():
    n = int(input())
    lst = tuple(map(int, input().split(" ")))
    win = int(input())
    find_max(lst, win)


if __name__ == "__main__":
    main()
