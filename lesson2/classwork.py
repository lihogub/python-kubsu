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

task1()
