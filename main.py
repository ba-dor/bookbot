f = open('books/frankenstein.txt', 'r')
file_contents = f.read()
file_contents_split = file_contents.split()
word_count = 0
word_count = len(file_contents_split)
print(word_count)
