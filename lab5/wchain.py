def read_file():
    words = []
    for line in open("in.txt"):
        new_line = line.strip("\n")
        words.append(new_line)
    words.sort(key=lambda index: len(index))
    return words


def difference(first_word, second_word):
    count = 0
    first_word_count, second_word_count = 0, 0
    while first_word_count < len(first_word) and second_word_count < len(second_word):
        if first_word[first_word_count] != second_word[second_word_count]:
            count += 1
            second_word_count -= 1
        first_word_count += 1
        second_word_count += 1
    return count


if __name__ == "__main__":
    next_word = read_file()
    # add first word by default
    result = [next_word.pop(0)]

    for word in next_word:
        previous_difference = 0
        previous_added = result[-1]

        if len(word) - len(previous_added) == 1:
            previous_difference = difference(word, previous_added)
            if previous_difference <= 1:
                result.append(word)

        if len(word) == len(previous_added):
            previous_difference = difference(word, result[-2])
            if previous_difference <= 1:
                result.pop()
                result.append(word)
    print("Supposed chain of words: ")
    print(result)
    result_file = open("out.txt", 'w')
    result_file.write(str(len(result)))
