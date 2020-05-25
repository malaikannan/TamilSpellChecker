# Tamil Spell Checker

Idea for building simple Tamil Spell Checker came from a conversation with T Shrinivasan from open-tamil team. 

Tamil Spell Checker uses below approach to suggest different spellings for a word

- Check whether it is a valid Tamil word using Bloom Filter
- Use Levenstein Distance (edit distance of 2) to suggest words when it is not a tamil word 

## Project Madurai Crawler

Project Madurai has good collection of tamil works. Use Project Madurai Crawler to generate Tamil unique word list. 

To run it use the below command 
,,,
python ProjectMaduraiCrawler.py
,,,

## Create Bloom Filter File 

Bloom Filter is a space efficient and compute optimized probablistic datastructure designed to tell whether an item is present in a set or not. More information on Bloom Filter can be found in [wiki](https://en.wikipedia.org/wiki/Bloom_filter).

- Spellchecker is using Bloom Filter to check whether a word is a valid tamil word or not. 
- Bloom Filter Datastructure file has to be created first before using to check validity of a word 

To generate Bloom Filter file use the below command 

,,,
python TamilBloomFilterCreator.py
,,,

## Sample code to check whether a word is valid tamil word

,,,
from TamilwordChecker import TamilwordChecker
unique_word_count = 2043478
tamilwordchecker = TamilwordChecker(unique_word_count,"tamil_bloom_filter.txt")
print(tamilwordchecker.tamil_word_exists("மேகம்"))
,,,

## Sample code to check get spell check corrections 

,,,
from TamilSpellingAutoCorrect import TamilSpellingAutoCorrect
spellchecker  = TamilSpellingAutoCorrect("tamil_bloom_filter.txt","tamilwordlist.txt")
from_spell_checker_list = spellchecker.tamil_correct_spelling("மேக்ம்")
print(from_spell_checker_list)
,,,



