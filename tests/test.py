import unittest
import timeit
from tamilspellchecker.TamilwordChecker import TamilwordChecker
from tamilspellchecker.TamilSpellingAutoCorrect import TamilSpellingAutoCorrect,get_data

unique_word_count = 2043478
timer = timeit.Timer()

#####To check whether word exist or not using Bloom Filter ############
class TamilSpellerTest(unittest.TestCase):
    def setUp(self):
        self.tamilwordchecker = TamilwordChecker(unique_word_count,get_data("tamil_bloom_filter.txt"))
        self.spellchecker  = TamilSpellingAutoCorrect(get_data("tamil_bloom_filter.txt"),get_data("tamilwordlist.txt"))

    def test_version(self):
        from tamilspellchecker import VERSION
        self.assertGreaterEqual(float(VERSION),0.10)

    def test_megam_bloomfilter_dictionary(self):
        self.assertTrue(self.tamilwordchecker.tamil_word_exists("மேகம்") , "Bloom Filter file is not proper")
        print(self.tamilwordchecker.tamil_word_exists("மேகம்"))
        #####To check whether word exist or not using Bloom Filter ############
        self.assertFalse( self.tamilwordchecker.tamil_word_exists("hello") , "Bloom Filter file is not proper")
        print(self.tamilwordchecker.tamil_word_exists("hello"))

    def test_autocorrect_dictionary_incorrectword(self):
        suggested_spell_checker_list = ['மேட்ம்', 'மேகநம்', 'மேகம்', 'மேகாம்', 'மேகும்', 'மேன்ம்']
        s_time = timer.timer()
        from_spell_checker_list = self.spellchecker.tamil_correct_spelling("மேக்ம்")
        print("Full search @/ incorrect word|Time ={0}".format( timer.timer() - s_time) )
        self.assertListEqual( sorted(suggested_spell_checker_list), sorted(from_spell_checker_list), "Auto correct is not proper")

    def test_autocorrect_dictionary_correctword(self):
        suggested_spell_checker_list = []
        s_time = timer.timer()
        from_spell_checker_list = self.spellchecker.tamil_correct_spelling("மேகம்")
        print("Full search @ w/ correct word|Time ={0}".format( timer.timer() - s_time ) )
        self.assertListEqual( sorted(suggested_spell_checker_list), sorted(from_spell_checker_list), "Auto correct is not proper")

    def test_autocorrect_norvig_correctword(self):
        suggested_word = 'மேகம்'
        s_time = timer.timer()
        from_spell_checker_list = self.spellchecker.tamil_Norvig_correct_spelling("மேகம்")
        print("Norvig @ w/ correct word|Time ={0}".format( timer.timer() - s_time ) )
        #print(from_spell_checker_list)
        self.assertTrue(  len(from_spell_checker_list) == 0, "Auto correct is not proper")

    def test_autocorrect_norvig_incorrectword(self):
        suggested_word = 'மேகம்'
        s_time = timer.timer()
        from_spell_checker_list = self.spellchecker.tamil_Norvig_correct_spelling("மேக்ம்")
        print("Norvig @ w/ incorrect word|Time ={0}".format( timer.timer() - s_time ) )
        #print(from_spell_checker_list)
        self.assertIn( suggested_word, from_spell_checker_list, "Auto correct is not proper")

if __name__ == "__main__":
    unittest.main()
