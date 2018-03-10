class StringProcessor(object):
    def __init__(self, string):
        """Create a StringProcessor object. When creating, takes a string."""
        self.string = string

    def clean(self, string):
        out_string = ''
        unwanted_character_list = ['.', ',']

        for character in string:
            if character not in unwanted_character_list:
                out_string += character

        out_string = out_string.lower()

        return out_string

    def tokenize(self):
        """Return a TokenManipulator object
        and pass it a list of tokens from our string."""

        cleaned_string = self.clean(self.string)
        tokens = cleaned_string.split()
        return TokenManipulator(tokens)


class TokenManipulator(object):
    def __init__(self, tokens):
        """Create the TokenManipulator object.
        When creating the object, we need to give it a list of tokens."""

        self.tokens = tokens

    def length(self):
        """Return the number of tokens in the token list."""
        return len(self.tokens)

    def count_match(self, match_string):
        """Count the words in the tokens list that match match_string."""

        word_match_counter = 0

        for word in self.tokens:
            if word == match_string:
                word_match_counter += 1

        return word_match_counter

    def match_first_character(self, match_character):
        words_beginning_with_character = []

        for word in self.tokens:
            if word[0] == match_character:
                words_beginning_with_character.append(word)

        return words_beginning_with_character


if __name__ == '__main__':
    original_text = "Everything should be built top-down, except the first time."

    processor = StringProcessor(original_text)

    tokens = processor.tokenize()

    print("Total words:",
          tokens.length())

    print('Number of occurances of word match:',
          tokens.count_match('except'))

    print("Words beginning with character:",
          tokens.match_first_character('e'))

    print("Number of words beginning with character:",
          len(tokens.match_first_character('e')))
