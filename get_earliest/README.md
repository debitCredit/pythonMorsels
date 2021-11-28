## Problem Statement

This exercise includes 1 bonuses and 6 hints (hover over the hint links before clicking on them).

This exercise is a somewhat silly one. I'd like you to compare the date strings, but allow invalid dates while comparing them.

I want you to write a function that takes two strings representing dates and returns the string that represents the earliest point in time. The strings are in the US-specific MM/DD/YYYY format... just to make things harder. Note that the month, year, and day will always be represented by 2, 4, and 2 digits respectively.

Your function should work like this:
```
>>> get_earliest("01/27/1832", "01/27/1756")
'01/27/1756'
>>> get_earliest("02/29/1972", "12/21/1946")
'12/21/1946'
>>> get_earliest("02/24/1946", "03/21/1946")
'02/24/1946'
>>> get_earliest("06/21/1958", "06/24/1958")
'06/21/1958'
```
There's a catch though. Your exercise should work with invalid month and date combinations. What I mean by that is that dates like 02/40/2006 should be supported. By that I mean 02/40/2006 is before 03/01/2006 but after 02/30/2006 (dates don't roll over at all). I'm adding this requirement so you can't rely on Python's datetime module.

There are many ways to solve this. See if you can figure out the clearest and most idiomatic way to solve this exercise. ✨

**Bonus**

If you complete the main exercise, there's also a bonus for you to attempt: allow the function to accept any number of arguments and return the earliest date string of all provided. ✔️

So if you complete the bonus, this should work:
```
>>> get_earliest("02/24/1946", "01/29/1946", "03/29/1945")
'03/29/1945'
```