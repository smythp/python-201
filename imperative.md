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
