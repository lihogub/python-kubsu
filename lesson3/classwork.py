# Input: N pairs of synonyms, word. Output: synonym for last input word
def task01():
    ABMap = {}
    n = int(input("N:"))
    for i in range(n):
        A, B, *_ = input().split()
        ABMap[A] = B
        ABMap[B] = A
    T = input()
    if T in ABMap:
        print(ABMap[T])
    else:
        print("Nope")
