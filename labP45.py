#Q.45 Program to find all anagrams and group them together from a given list of string.
from collections import defaultdict

def group_anagrams(word_list):
    anagram_dict = defaultdict(set)

    for word in word_list:
        key = ''.join(sorted(word))
        anagram_dict[key].add(word)

    return list(anagram_dict.values())

words = ["bat", "tab", "tap", "pat", "cat", "act", "tac"]
result = group_anagrams(words)

print("Grouped Anagrams:")
for group in result:
    print(group)

