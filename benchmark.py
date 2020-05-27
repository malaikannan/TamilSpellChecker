from TamilwordChecker import TamilwordChecker
import traceback
import datetime

def read_tamil_words_list_file(tamil_unique_word_list_file_path,benchmark_count):

    ta_words_unique = []
    unique_word_count = 0
    try:
        tamil_word_file = open(tamil_unique_word_list_file_path, 'r') 
        for line in tamil_word_file: 
            ta_words_unique.append(line.strip())
            unique_word_count = unique_word_count + 1
        tamil_word_file.close()    
    except Exception as e:
        track = traceback.format_exc()
        print(track)
    return ta_words_unique[0:benchmark_count]

if __name__ == "__main__":
    number_of_words = 10000
    ta_words_unique = read_tamil_words_list_file("unique_sorted_words_in_words_master.txt",number_of_words)
    tamilwordchecker = TamilwordChecker(2392064,"tamil_bloom_filter_allwords.txt")
    total_time_diff = 0
    for word in ta_words_unique:
        start_time = datetime.datetime.now()
        flag = tamilwordchecker.tamil_word_exists(word)
        #print(f"{word} tamil word exists : {flag}")
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        total_time_diff = total_time_diff + execution_time
        #print(f"Time taken to check {word} exist or not in milli seconds ", execution_time)

    average_time = total_time_diff/number_of_words
    print(f"Average time taken to check word exist or not for {number_of_words} words is {average_time}")
    
    #Average time taken to check word exist or not for 10000 words is 0.032965399999999485