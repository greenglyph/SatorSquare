from collections import defaultdict
from itertools import product

palindromes = defaultdict(list)
# a dict in the form of {wordLength:word}
# 'palindrome' here refers to a single word that is identical to itself when
#  spelled backwards, e.g. 'radar'

emordnilaps = defaultdict(lambda: defaultdict(list))
# a nested dict in the form of
# {wordLength: {'middleLetter': ['word1','word2',...]}}
# 'emordnilap' here refers to a single word that spells a different word when
# spelled backwards, e.g. 'deifier' and 'reified'

word_file = open ('sowpods.txt', 'r')
candidate_words = []
sator_squares = []


def is_palindrome(word):
    """Test whether a word is a palindrome by comparing it to a reversed version of itself"""
    if len(word) % 2 != 0 and word == word[::-1]:
        return True
    else:
        return False


def is_emordnilap(word):
    """Test whether a reversed word appears in a list of words"""
    # this is very slow. use better search algorithm (binary)?
    if len(word) % 2 != 0 and word != word[::-1] and word[::-1] in candidate_words:
        return True
    else:
        return False


def find_sator_squares(word_length, palindrome):
    sator_components = []
    letter_index = 0
    while letter_index < word_length/2:
        if emordnilaps[word_length][palindrome[letter_index]] == []:
            #try/catch instead?
            return
        else:
            sator_components.append(emordnilaps[word_length][palindrome[letter_index]])
        letter_index += 1
    print(palindrome, sator_components)


for word in word_file:
    candidate_words.append(word.rstrip('\r\n'))

for word in candidate_words:
    if is_palindrome(word):
        palindromes[len(word)].append(word)
    elif is_emordnilap(word):
        emordnilaps[len(word)][word[int(len(word)/2)]].append(word)

for length in palindromes:
    # replace 'key' and 'value' with 'length' and 'word'?
    for word in palindromes[length]:
        find_sator_squares(length, word)
