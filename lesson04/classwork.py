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

