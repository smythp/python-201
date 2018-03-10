def not_unwanted_character(unwanted_list):
    """Return a function that returns a character if it's not on an unwanted character list."""

    def unwanted_character_closure(character):
        if character not in unwanted_list:
            return character

    return unwanted_character_closure


def remove_characters(string, unwanted_character_list):
    """Return a string with the unwanted characters removed."""

    filtered = filter(
        not_unwanted_character(unwanted_character_list), string)

    cleaned_string = ''.join(list(filtered))

    return cleaned_string


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


def is_matching_word(word_to_match):
    """Return a function that returns a given word only if it matches."""
    def word_closure(word):
        if word == word_to_match:
            return word

    return word_closure


def count_word_occurances(word_list, word_to_match):
    """Returns the number of occurances of word in the string."""

    matching_words = filter(is_matching_word(word_to_match), word_list)

    length = len(list(matching_words))

    return length


def is_matching_first_character(character):
    """Return a function that returns a word only if it begins with a certain character."""

    def character_closure(word):
        if word[0] == character:
            return word

    return character_closure


def words_matching_first_character(word_list, match_character):
    """Return a list of words that begin with a particular character."""

    word_matches = filter(
        is_matching_first_character(match_character), word_list)

    return list(word_matches)


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
