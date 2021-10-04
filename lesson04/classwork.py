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
