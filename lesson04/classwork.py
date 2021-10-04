# Print word count
def task01():
    file = open("input1.txt", "r")
    lines = file.readlines()
    word_set = set()
    for line in lines:
        words = line.split()
        word_set.update(words)

    word_count = len(word_set)
    print(f"Word count: {word_count}")


# Print sum of each line
def task02():
    file = open("input2.txt", "r")
    lines = file.readlines()
    result = []
    for line in lines:
        numbers = list(map(int, line.split()))
        result.append(sum(numbers))
    print(f"Result: {result}")


# Print words in order of descending by count and then ascending lexicographically
def task03():
    file = open("input3.txt", "r")
    lines = file.readlines()
    words = dict()
    for line in lines:
        for word in line.split():
            if word in words:
                words[word] -= 1
            else:
                words[word] = -1

    count_word_list = sorted([(count, word) for word, count in words.items()])
    word_list = [word for count, word in count_word_list]
    result = " ".join(word_list)
    print(result)


# Print lines reversed
def task04():
    file = open("input4.txt", "r")
    lines = file.readlines()
    result = "".join(reversed(lines))
    print(result)


# Print line count, word count, symbol count
def task05():
    file = open("input5.txt", "r")
    lines = file.readlines()
    word_set = set()
    symbol_set = set()
    for line in lines:
        for word in filter(str.isalpha, line.split()):
            word_set.add(word)
            symbol_set.update(word)

    count_lines = len(lines)
    count_words = len(word_set)
    count_symbols = len(symbol_set)

    print(f"Lines: {count_lines}\nWords: {count_words}\nSymbols: {count_symbols}")
