def stack_max(_lst):
    if len(_lst) == 0:
        return
    max_stack = [0]
    for req in _lst:
        if req[0] == "push":
            num = int(req[1])
            if max_stack[-1] < num:
                max_stack.append(num)
            else:
                max_stack.append(max_stack[-1])
        else:
            if req[0] == "pop":
                max_stack.pop()
            else:
                print(max_stack[-1])


def main():
    n = int(input())
    lst = tuple(tuple(input().split()) for i in range(n))
    stack_max(lst)


if __name__ == "__main__":
    main()

