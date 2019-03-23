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
        
        ####
        check if not exists
            true -> 
                set min_value to 1. 
                add 1 to key_to_value[key]
                add key to value_to_key[1]
                if max_value == 0: max_value = 1

            false -> 
                old_value = key_to_value[key]
                new_value = old_value + 1

                remove from value_to_key[old_value]
                add to value_to_key[new_value]

                if new_value > max_value: set max_value to new_value
                
                if old_value == min_value and there is no other key in valueToKey[old_value]: set min_value to new_value
        """

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """

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

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()