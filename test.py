from TamilwordChecker import TamilwordChecker

#####To check whether word exist or not using Bloom Filter ############
tamilwordchecker = TamilwordChecker(2043478,"tamil_bloom_filter.txt")
assert tamilwordchecker.tamil_word_exists("மேகம்") == True, "Bloom Filter file is not proper"
print(tamilwordchecker.tamil_word_exists("மேகம்"))

#####To check whether word exist or not using Bloom Filter ############
assert tamilwordchecker.tamil_word_exists("hello") == False, "Bloom Filter file is not proper"
print(tamilwordchecker.tamil_word_exists("hello"))



