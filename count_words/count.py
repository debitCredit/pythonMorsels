from collections import defaultdict, Counter
import re


def count_words(s: str):
    return Counter(re.findall(r"\b[\w'-]+\b", s.lower()))
