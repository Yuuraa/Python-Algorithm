class MyHashMap:
    def __init__(self):
        self.keys = []
        self.vals = []

    def put(self, key, value):
        if key in self.keys:
            idx = self.keys.index(key)
            self.vals[idx] = value
        else:
            self.keys.append(key)
            self.vals.append(value)
    
    def get(self, key):
        if key in self.keys:
            idx = self.keys.index(key)
            return self.vals[idx]
        else:
            return -1
    
    def remove(self, key):
        if key in self.keys:
            idx = self.keys.index(key)
            self.keys.pop(idx)
            self.vals.pop(idx)


class OthersHashmap:
    def __init__(self):
        self.hashmap = []

    def put(self, key, value):
        added = False
        for i, (k, v) in enumerate(self.hashmap):
            if k == key:
                self.hashmap[i] = (key, value)
                added = True
        if not added:
            self.hashmap.append((key, value))

    def get(self, key):
        for k, v in self.hashmap:
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, (k, v) in enumerate(self.hashmap):
            if k == key:
                del self.hashmap[i]
        

def test_hasmap(hashMap):
    result = []
    hashMap.put(1, 1)        
    hashMap.put(2, 2)        
    result.append(hashMap.get(1)) # 1
    result.append(hashMap.get(3)) # -1
    hashMap.put(2, 1)
    result.append(hashMap.get(2)) # 1
    hashMap.remove(2)        
    result.append(hashMap.get(2)) # -1   
    return result
    


if __name__ == "__main__":
    # hashMap = MyHashMap()
    hashMap = OthersHashmap()
    assert(test_hasmap(hashMap) == [1, -1, 1, -1])
    print("All examples passed")