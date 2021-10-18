import codecs
import re


def task01():
    file = codecs.open("individual_task_03.txt", "r", "utf-8")
    lines = file.readlines()
    word_list = []

    pattern = r'[a-zA-Z]+'
    for line in lines:
        for word in re.findall(pattern, line):
            word_list.append(word)

    first_letter = lines[0].split()[0]
    print(first_letter)

    target_words = lines[1].split()
    target_words_count = {}
    for word in target_words:
        target_words_count[word] = 0
    if word_list[0] in target_words:
        target_words_count[word_list[0]] += 1

    starts_with = 0
    for word in word_list:
        if word.startswith(first_letter):
            starts_with += 1
        if word in target_words:
            target_words_count[word] += 1

    times_in_row = 0
    for i in range(1, len(word_list)):
        if (word_list[i] in target_words) and (word_list[i - 1] in target_words) and (word_list[i] != word_list[i - 1]):
            times_in_row += 1
    print(f"Target words: {target_words_count}. \nStarts with: {starts_with}. \nTwo times in row: {times_in_row}.")


task01()
