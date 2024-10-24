def get_word_count(file_contents):
    word_count = 0
    split_file_contents = file_contents.split()
    word_count = len(split_file_contents)
    return word_count

def get_char_count(file_contents):
    character_count = {}
    file_contents_lower = file_contents.lower()
    print(file_contents_lower)
    file_contents_words = file_contents_lower.split()
    for i in range(len(file_contents_words)):
        for char in file_contents_words[i]:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count
    # sort:
    # return dict(sorted(character_count.items()))

f = open('books/frankenstein.txt', 'r')
file_contents = f.read()
print(get_char_count(file_contents))