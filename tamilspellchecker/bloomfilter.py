import math

import mmh3
from bitarray import bitarray


class BloomFilter(object): 

    ''' 
    Class for Bloom filter, using murmur3 hash function 
    '''

    def __init__(self, items_count,falsepositive_probability,file_path = None): 
        ''' 
        items_count : int 
        Number of items expected to be stored in bloom filter 
        fp_prob : float 
        False Positive probability in decimal 
        '''
        # False posible probability in decimal 
        self.falsepositive_probability = falsepositive_probability 

        #Number of items to be stored
        self.items_count = items_count

        # Size of bit array to use 
        self.get_size() 

        # number of hash functions to use 
        self.get_hash_count() 

         # initialize all bits as 0 
        if file_path is not None:
            with open(file_path,'r') as fb:
                str_bits = fb.read()
                self.bit_array = bitarray(str_bits)
        else:
            self.bit_array = bitarray(self.size,endian='little') 
            self.bit_array.setall(0) 


    def add(self, item): 
        ''' 
        Add an item in the filter 
        '''
        digests = [] 
        for i in range(self.hash_count): 

        # create digest for given item. 
            # i work as seed to mmh3.hash() function 
            # With different seed, digest created is different 
            digest = mmh3.hash(item,i) % self.size 
            digests.append(digest) 

            # set the bit True in bit_array 
            self.bit_array[digest] = True

    def check(self, item): 
        ''' 
        Check for existence of an item in filter 
        '''
        for i in range(self.hash_count): 
            digest = mmh3.hash(item,i) % self.size 
            if self.bit_array[digest] == False: 

            # if any of bit is False then,its not present 
            # in filter 
            # else there is probability that it exist 
                return False
        return True

    def writetofile(self, file_path): 
        ''' 
        Save to File  
        '''
        with open(file_path,'w') as fb:
            fb.write(self.bit_array.to01()) 
    
           
    def get_size(self): 
        ''' 
        Return the size of bit array(size) to used using 
        following formula 
        size = -(items_count * lg(falsepositive_probability)) / (lg(2)^2) 
        '''
        self.size = int(-(self.items_count * math.log(self.falsepositive_probability))/(math.log(2)**2)) 
         

    def get_hash_count(self): 
        ''' 
        Return the hash function(hash_count) to be used using 
        following formula 
        hash_count = (size/items_count) * lg(2) 
        '''
        self.hash_count = int((self.size/self.items_count) * math.log(2)) 
 