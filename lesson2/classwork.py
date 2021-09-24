from functools import reduce


# print union, intersection and difference of color sets
def task1():
    child1 = set(input("Child 1: ").split())
    child2 = set(input("Child 2: ").split())

    colors_union = child1.union(child2)
    colors_intersect = child1.intersection(child2)
    colors_diff = child1.difference(child2)

    print(len(colors_union), colors_union)
    print(len(colors_intersect), colors_intersect)
    print(len(colors_diff), colors_diff)


# children languages, languages count -> languages union, languages intersection
def task2():
    children_count = int(input("Children count: "))

    child_0 = set(input("Child 0: ").split())
    lang_set_all = set(child_0)
    lang_set_any = set(child_0)

    for i in range(1, children_count):
        child_tmp = set(input("Child " + str(i) + ": ").split())
        lang_set_all.intersection_update(child_tmp)
        lang_set_any.update(child_tmp)

    print(lang_set_any)
    print(lang_set_all)


# day count, party break start day, party break count day
# every first day is break
# weekend is free
def task3():
    days = int(input("Days: "))
    party_count = int(input("Party count: "))
    free_days = set()

    for i in range(6, days + 1, 7):
        free_days.add(i)
    for i in range(7, days + 1, 7):
        free_days.add(i)

    for i in range(1, party_count + 1):
        start, step = map(int, input("Party " + str(i) + ": ").split())
        for day in range(start, days + 1, step):
            free_days.add(day)

    print(free_days)
    print(days - len(free_days))


task3()
