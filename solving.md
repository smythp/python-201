# Comparing Solutions

Imagine that we have a block of text in the form of a string and we want to perform a basic analysis on it. We want to know:

1. How many words are in the string.
2. How many occurrences of certain words there are.
3. What words, and how many, start with a certain letter.

In the process of looking for these items, we'll also have to clean the string by removing commas and periods and making it lowercase, in addition to splitting it up into a list of words.

# Imperative Solution

Remember that the imperative solution defines a series of steps to go through to solve the problem. Our first step is to define the data we'll be working with—in the real world we'd probably be pulling this text in from another source, but here we'll create a short block of text right in the program.

```python
original_text = "Everything should be built top-down, except the first time."
```
	
Then let's define the characters we want to remove in a list:

```python
unwanted_characters = [',', '.']
```
	
It's possible to loop through a list just like we loop through a string. Let's do that and build a new string that doesn't have the characters we don't want:

```python
for character in original_text:
    if character not in unwanted_characters:
        string_without_punctuation += character
```

Let's make the string all lower case:

```python
string_lower_case = string_without_punctuation.lower()
```

and split the string into a list:

```python
word_list = string_lower_case.split()
```
Now that we have our list, let's start answering questions. First, how many words are there in total?

```python
word_list_length = len(word_list)
print("Total words:", word_list_length)
```

Let's answer the question of how many occurances of a certain word there are. Let's try searching for "except."

```python
word_to_search = 'except'
word_match_counter = 0

for word in word_list:
    if word == word_to_search:
        word_match_counter += 1

print('Number of occurances of word match:', word_match_counter)
```

Finally, we need to get all the words that start with a certain character, and then check how many of those words there are:

```python
match_character = 'e'
words_beginning_with_character = []

for word in word_list:
    if word[0] == match_character:
        words_beginning_with_character.append(word)

print("Words beginning with character:", words_beginning_with_character)
print("Number of words beginning with character:",
      len(words_beginning_with_character))
```

When run, our prigram will print out the information we want about our short piece of text. Our full imperative script can be viewed [here](imperative.py).

## Problems With An Imperative Approach

You may already be seeing some issues with the imperative approach. First, our code is pretty messy. The script does a bunch of things, and we don't know which part of the script is dedicated to which functionality. Second, it's not very reusable. If we try to do another analysis, we'll be changing variables or copy and pasting code, which violates the programming principle of DRY—don't repeat yourself. Third, if we need to change the program, there are many parts that are dependent on other parts, which means that one change is likely to require a bunch of other changes to accommodate it.

# Introducing Functional Programming

Functional programming is a programming paradigm that solves problems by moving data from function to function, resulting in a series of transformations. Functional programming recognizes that a source of complexity in programs is the assignment of variables, since assigning variables means that the designer of the program, and the program itself, can't be sure what state the variable is in when it's used. In pure functional programming, variables are not used at all, and everything is done by passing values between functions. In Python, functional programming usually means keeping variable assignment within functions and not defining variables outside functions.

Let's try rewriting our analysis in a more functional style.

## Functional Solution

Let's first try moving the part of our script that removes unwanted characters into a function:

```python
def remove_characters(string, unwanted_character_list):
    "Takes unwanted characters as a list and removes them from a string."
    out_string = ''

    for character in string:
        if character not in unwanted_character_list:
            out_string += character

    return out_string
```	

Notice that there is a string after the function definition that tells us what the function does. This is called a "docstring"—it's used to document our functions and can be used to automatically build documentation for our program after we've finished writing it, assuming we want to publish the code and share it with others.

Our function does much the same as the imperative code, but serves a few purposes. First, it marks out the purpose of this section of code, making it easier to know what each line of code is for. Second, it can be reused in other parts of the program. Third, it makes the transformation that it's performing clearer—if we know what comes in and what comes out of each function, it's easier to reason about our program and the transformations it's making.

Let's replicate the rest of our imperative program as functions:

```python
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
```	

These functions don't make assumptions about what string or list of words will be processed, so they can easily be reused. Notice how the `clean_string` function incorporates the `remove characters` function. If we were to add more steps to processing our string, such as removing extra whitespace or deleting commonly used words such as articles, we could just add those steps into the `clean_string` function. Because we've written other parts of the code based on function outputs, rather than specific variables, we can make changes that are less likely to break the code as long as we make sure our functions return the same kind of output.

Notice that our `tokenize` function takes an argument that looks like this `preprocess=False`. This means that, if we leave off that argument, the tokenize function won't clean the string first—that's our default option. But we can also choose to add `True` as an arugment, which means our string will be processed with our `clean_string` function before it is split into a list of words.

Finally, let's use our functions to create output similar to our imperative code:

```python
if __name__ == '__main__':
    original_text = "Everything should be built top-down, except the first time."
    tokens = tokenize(original_text, True)

    print("Total words:", len(tokens))

    print('Number of occurances of word match:',
          count_word_occurances(tokens, 'except'))

    print("Words beginning with character:",
          words_matching_first_character(tokens, 'e'))

    print("Number of words beginning with character:",
          words_matching_first_character(tokens, 'e'))
```

The `if __name__ == '__main__':` portion of the code means that the code after it will only be run if our script is run directly. If it's imported like a library, this part won't run. Mostly, this code just calls the functions we've defined in order to print some results.

You can see our full functional code [here](functional.py). Next, we'll be looking at object-oriented programming, which takes a very different approach to using state in solving problems.

# Object-Oriented Programming

Object-oriented, or OO, programming doesn't try to avoid state like functional programming does. Instead, it combines functions and state together into something called an object. An object in object-oriented programming is a container for some data and functions that work on that data.

If functional programming is all about keeping data and functions separate, object-oriented programming connects functions and data together.

## Functional Solution

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


        words_beginning_with_character = []

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
