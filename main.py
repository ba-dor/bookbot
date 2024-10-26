def get_word_count(file_contents):
    word_count = 0
    split_file_contents = file_contents.split()
    word_count = len(split_file_contents)
    return word_count

def get_char_count(file_contents):
    character_count = {}
    file_contents_lower = file_contents.lower()
    file_contents_words = file_contents_lower.split()
    for i in range(len(file_contents_words)):
        for char in file_contents_words[i]:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    # Unsorted:
    # return character_count
    # Sort alphabetically:
    # return dict(sorted(character_count.items()))
    # Sort by value:
    return dict(sorted(character_count.items(),key=lambda x:x[1], reverse=True))

book_path = 'books/frankenstein.txt'
f = open(book_path, 'r')
file_contents = f.read()
char_count = get_char_count(file_contents)

print(f"--- Begin report of {book_path} ---")
print(f"{get_word_count(file_contents)} words found in the document\n")
for item in char_count:
    print(f"The '{item}' character was found {char_count[item]} times")
