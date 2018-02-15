original_text = "Everything should be built top-down, except the first time."

unwanted_characters = [',', '.']

string_without_punctuation = ''

for character in original_text:
    if character not in unwanted_characters:
        string_without_punctuation += character


string_lower_case = string_without_punctuation.lower()

word_list = string_lower_case.split()

word_list_length = len(word_list)
print("Total words:", word_list_length)

word_to_search = 'except'
word_match_counter = 0

for word in word_list:
    if word == word_to_search:
        word_match_counter += 1

print('Number of occurances of word match:', word_match_counter)

match_character = 'e'
words_beginning_with_character = []

for word in word_list:
    if word[0] == match_character:
        words_beginning_with_character.append(word)

print("Words beginning with character:", words_beginning_with_character)

print("Number of words beginning with character:",
      len(words_beginning_with_character))
