def remove_characters(string, unwanted_character_list):
    "Takes unwanted characters as a list and removes them from a string."
    out_string = ''

    for character in string:
        if character not in unwanted_character_list:
            out_string += character

    return out_string


def clean_string(string):
    "Process and clean a string for tokenization."
    string_without_punctuation = remove_characters(string, ['.', ','])
    string_lower_case = string_without_punctuation.lower()

    return string_lower_case


def tokenize(string, preprocess=False):
    """Make string into list of words. \
    If preprocess is True, clean the string first."""
    if preprocess:
        string = clean_string(string)

    word_list = string.split()

    return word_list


def count_word_occurances(word_list, word_to_match):
    """Returns the number of occurances of word in the string."""
    word_match_counter = 0

    for word in word_list:
        if word == word_to_match:
            word_match_counter += 1

    return word_match_counter


def words_matching_first_character(word_list, match_character):

    words_beginning_with_character = []

    for word in word_list:
        if word[0] == match_character:
            words_beginning_with_character.append(word)

    return words_beginning_with_character


if __name__ == '__main__':
    original_text = "Everything should be built top-down, except the first time."
    tokens = tokenize(original_text, True)

    print("Total words:", len(tokens))

    print('Number of occurances of word match:',
          count_word_occurances(tokens, 'except'))

    print("Words beginning with character:",
          words_matching_first_character(tokens, 'e'))

    print("Number of words beginning with character:",
          len(words_matching_first_character(tokens, 'e')))
