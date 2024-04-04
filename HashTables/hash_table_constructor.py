class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size # create empty list of size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

hash_table = HashTable()
hash_table.print_table()