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


# print minimal distance between local maximums of list
def three(_list):
    l_max_list = []

    for i in range(1, len(_list) - 1):
        if (_list[i-1] < _list[i]) and (_list[i] > _list[i+1]):
            l_max_list.append(i)

    l_dist = len(_list)

    for i in range(1, len(l_max_list)):
        l_dist = min(l_dist, l_max_list[i] - l_max_list[i-1])

    if l_dist == len(_list):
        print("Not enough maximums")
    else:
        print(l_dist)
