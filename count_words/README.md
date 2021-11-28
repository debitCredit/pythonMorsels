## Problem Statement

This exercise includes 2 bonuses and 5 hints (hover over the hint links before clicking on them).

When solving this exercise, make sure to hold off on searching directly for the answer on Google/StackOverflow. 🚫🔍

This is a fairly general exercise and there are a number of answers to it. I'd like you to struggle to come to an answer or two (or five?) on your own.

I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.

Your function should work like this:
```
>>> count_words("oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
>>> count_words("don't stop believing")
{"don't": 1, 'stop': 1, 'believing': 1}
```

**Bonus 1**

As a bonus, make sure your function works well with mixed case words:
```
>>> count_words("Oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
Bonus 2
```
For even **more of a bonus** try to get your function to ignore punctuation outside of words:
```
>>> count_words("Oh what a day, what a lovely day!")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
```