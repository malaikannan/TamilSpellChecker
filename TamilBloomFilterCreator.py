from bloomfilter import BloomFilter
import os
import traceback

class TamilBLoomFilterCreator:

    def __init__(self,false_positive_probability,bloom_file_path,tamil_unique_word_list_file_path):

        self.false_positive_probability = 0.001
        self.bloom_file_path = bloom_file_path
        self.tamil_unique_word_list_file_path = tamil_unique_word_list_file_path
        self.read_tamil_words_list_file()
   
    def read_tamil_words_list_file(self):
    
        self.ta_words_unique = []
        self.unique_word_count = 0
        try:
            tamil_word_file = open(self.tamil_unique_word_list_file_path, 'r') 
            for line in tamil_word_file: 
                self.ta_words_unique.append(line.strip())
                self.unique_word_count = self.unique_word_count + 1
            tamil_word_file.close()    
        except Exception as e:
            track = traceback.format_exc()
            print(track)


    def create_bloomfilter_file(self):
            
            bloomf = BloomFilter(self.unique_word_count,self.false_positive_probability) 
            try:
                for word in self.ta_words_unique:
                    bloomf.add(word)
                bloomf.writetofile(self.bloom_file_path)
            except Exception as e:
                track = traceback.format_exc()
                print(track)

if __name__ == "__main__":
    
    bloomcreator  = TamilBLoomFilterCreator("0.001","tamil_bloom_filter_allwords.txt","unique_sorted_words_in_words_master.txt")
    bloomcreator.create_bloomfilter_file()


