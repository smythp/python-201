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
