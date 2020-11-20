import datetime

from bloomfilter import BloomFilter


class TamilwordChecker:

    def __init__(self,unique_word_count, bloomfilter_file_path):
        falsepositive_probability = 0.001
        self.bloom_tamil = BloomFilter(unique_word_count,falsepositive_probability,bloomfilter_file_path)

    def tamil_word_exists(self,word):
        if self.bloom_tamil.check(word):
            return True
        else:
            return False
    

if __name__ == "__main__":
    tamilwordchecker = TamilwordChecker(2392064,"tamil_bloom_filter_allwords.txt")
    start_time = datetime.datetime.now()
    print(" மேகம் tamil word exists : ",tamilwordchecker.tamil_word_exists("மேகம்"))    
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print("Time taken to check மேகம் exist or not in milli seconds ", execution_time)
    start_time = datetime.datetime.now()
    print("தமிழ் tamil word exists : ",tamilwordchecker.tamil_word_exists("தமிழ்"))    
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print("Time taken to check தமிழ் exist or not in milli seconds ", execution_time)
    start_time = datetime.datetime.now()
    print("டாமில் tamil word exists : ",tamilwordchecker.tamil_word_exists("டாமில்"))    
    print(tamilwordchecker.tamil_word_exists("டாமில்"))    
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print("Time taken to check hello exist or not in milli seconds ", execution_time)
    
