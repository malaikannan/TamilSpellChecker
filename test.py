import unittest

from TamilwordChecker import TamilwordChecker

#####To check whether word exist or not using Bloom Filter ############
tamilwordchecker = TamilwordChecker(2043478,"tamil_bloom_filter.txt")
assert tamilwordchecker.tamil_word_exists("மேகம்") == True, "Bloom Filter file is not proper"
print(tamilwordchecker.tamil_word_exists("மேகம்"))

#####To check whether word exist or not using Bloom Filter ############
assert tamilwordchecker.tamil_word_exists("hello") == False, "Bloom Filter file is not proper"
print(tamilwordchecker.tamil_word_exists("hello"))

from TamilSpellingAutoCorrect import TamilSpellingAutoCorrect
spellchecker  = TamilSpellingAutoCorrect("tamil_bloom_filter.txt","tamilwordlist.txt")

suggested_spell_checker_list = ['மேட்ம்', 'மேகநம்', 'மேகம்', 'மேகாம்', 'மேகும்', 'மேன்ம்']
from_spell_checker_list = spellchecker.tamil_correct_spelling("மேக்ம்")
assert set(suggested_spell_checker_list) == set(from_spell_checker_list), "Auto correct is not proper" 

suggested_spell_checker_list = []
from_spell_checker_list = spellchecker.tamil_correct_spelling("மேகம்")
assert set(suggested_spell_checker_list) == set(from_spell_checker_list), "Auto correct is not proper" 






