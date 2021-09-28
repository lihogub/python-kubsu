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


# Input: string containing words. Output: each word changed to number it appeared previously
def task02():
    word_counter_map = {}
    result_list = []
    word_list = input("Input: ").split()
    for word in word_list:
        if word not in word_counter_map:
            result_list.append(0)
            word_counter_map[word] = 1
        else:
            result_list.append(word_counter_map[word])
            word_counter_map[word] += 1
    print("Input: " + str(result_list))


# Input: string containing words. Output: the most often word (return the least lexicographically if there are few same often words)
def task03():
    word_counter_map = {}
    word_list = input("Input: ").split()
    for word in word_list:
        if word not in word_counter_map:
            word_counter_map[word] = 1
        else:
            word_counter_map[word] += 1

    r = [(-val, key) for key, val in word_counter_map.items()]
    r.sort()
    print(r[0][1])
