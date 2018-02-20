[<<< Previous](functional.md)

# Object-Oriented Programming

Object-oriented, or OO, programming doesn't try to avoid state like functional programming does. Instead, it combines functions and state together into something called an object. An object in object-oriented programming is a container for some data and functions that work on that data.

If functional programming is all about keeping data and functions separate, object-oriented programming connects functions and data together.

## Object-Oriented Solution

In our functional solution, we created a set of functions that could talk with one another and which could pass data between them. Our object-oriented solution will create two object classes, one that processes text given to it as a string and another that manipulates a list of tokens. 

Our processor will have two "methods." Methods are a special term for a function that is inside an object. It will also have one attribute, which is a special term for a variable defined inside an object. The attribute will be our original text string. The methods will clean the string (making it lower case and without periods and commas) and tokenize it (turn it into a list of words), respectively.

Our other class object, the TokenManipulator, has an attribute that is a list of words. It also has methods that operate on the list of works, such as counting matches and returning a list of the words that begin with a certain letter.

Let's take a look at our two objects:

```python
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
        """Create the TokenManipulator ojbect.
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
```

Each object has an `__init__` method that is run when objects are created from the class. These usually define attributes inside the object based on arguments that are passed when the object is created. When you see the word `self` in a class, that refers to the object itself. `self.string` is an attribute—that is, a variable defined inside the object.

Let's use our classes to create objects that will answer questions about our string:

```python
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
```

In the object-oriented model, state is contained inside the object. Our StringProcessor object contains an attribute that represents a string. Our TokenManipulator object contains an attribute that represents a list of words. These objects also have methods, or functions defined inside them, that work on those attributes. Our `clean` method, for example, operates on the `string` attribute inside a StringProcessor object.

[<<< Previous](functional.md)

