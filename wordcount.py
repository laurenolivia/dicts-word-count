def get_word_count(file):  # initialize function that takes 1 arg as file
    """return word count from file"""
    word_count = {}
    with open(file) as txt_file:
        for line in txt_file:
            # line = line.strip()
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
            # print word_count

    return word_count


count_words = get_word_count("test.txt")
#dict.get(word, 0) +1
#return dictionary

for k, v in count_words.items():
    print "%s %d" % (k, v)
