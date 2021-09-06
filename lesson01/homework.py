# print quantity of monotonic fragments of list
def one(_list):
    stack = []
    c = 1

    for i in _list:
        if len(stack):
            if stack[-1] > i:
                c += 1
                stack.clear()
        stack.append(i)

    print(c)


# print quantity of local maximums of list
def two(_list):
    c = 0

    for i in range(1, len(_list) - 1):
        if (_list[i-1] < _list[i]) and (_list[i] > _list[i+1]):
            c += 1

    print(c)

