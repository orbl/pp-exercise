class AllOne:

    def __init__(self):        
        """
        Initialize your data structure here.
        """
        self.value_to_key = {}
        self.key_to_value = {}
        self.min_value = 0
        self.max_value = 0 
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key_to_value:
            old_value = self.key_to_value[key]
            new_value = old_value + 1

            self.remove_data_key(key, old_value)

            self.add_data_key(key, new_value)

            if new_value > self.max_value: 
                self.max_value = new_value
            
            if old_value == self.min_value and old_value not in self.value_to_key:
                self.min_value = new_value

            self.key_to_value[key] = new_value

        else:
            self.key_to_value[key] = 1  
            self.add_data_key(key, 1)

            if self.max_value == 0: 
                self.max_value = 1
            self.min_value = 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key_to_value:
            if self.key_to_value[key] == 1:
                self.remove_data_key(key, 1)
                del self.key_to_value[key]

                if len(self.key_to_value) == 0:
                    self.max_value = 0
                    self.min_value = 0
                elif 1 not in self.value_to_key:
                    self.min_value = min(self.value_to_key)
            else:
                old_value = self.key_to_value[key]
                new_value = old_value - 1

                self.remove_data_key(key, old_value)
                self.add_data_key(key, new_value)

                if new_value < self.min_value:
                    self.min_value = new_value
                
                if old_value == self.max_value and old_value not in self.value_to_key:
                    self.max_value = new_value

                self.key_to_value[key] = new_value

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_value == 0:
            return ""
        else:
            return next(iter(self.value_to_key[self.max_value]))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.min_value == 0:
            return ""
        else:
            return next(iter(self.value_to_key[self.min_value]))

    def add_data_key(self, key, new_value) -> None:
        """
        Helper method that handles adding to value_to_key
        sets
        """
        if new_value not in self.value_to_key:
            self.value_to_key[new_value] = set()

        self.value_to_key[new_value].add(key)

    def remove_data_key(self, key, old_value) -> None:
        """
        Helper method that handles removing from value_to_key
        sets
        """       
        self.value_to_key[old_value].remove(key)

        if len(self.value_to_key[old_value]) == 0:
            del self.value_to_key[old_value]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()