# print union, intersection and difference of color sets
from functools import reduce


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

    children_langs_list = [set(input("Child " + str(i) + ": ").split()) for i in range(children_count)]

    un = reduce(lambda prev, cur: prev.union(cur), children_langs_list, set())

    inter = reduce(lambda prev, cur: prev.intersection(cur), children_langs_list, children_langs_list[0])

    print(un)
    print(inter)


task2()
