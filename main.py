def get_word_count(file_contents):
    word_count = 0
    split_file_contents = file_contents.split()
    word_count = len(split_file_contents)
    return word_count

f = open('books/frankenstein.txt', 'r')
file_contents = f.read()
word_count = get_word_count(file_contents)
print(word_count)
