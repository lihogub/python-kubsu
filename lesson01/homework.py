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

