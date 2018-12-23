# encoding : utf-8
'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key)： - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
(如果存在，返回值；如果不存在，返回value)
put(key, value)： - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
（如果length<capacity,直接put，否则删除一个最近最少使用的
对于put，若key不存在，直接插入；否则重新赋值）

Follow up:
Could you do both operations in O(1) time complexity?
'''


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = {}
        # 排序（删除顺序），先进先出
        self.keys = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            index = self.keys.index(key)
            # 改变删除顺序
            self.keys.append(key)
            self.keys.pop(index)
            return self.hash[key]
        except Exception as e:
            print(e)
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.keys:
            self.hash[key] = value
            index = self.keys.index(key)
            # 改变删除顺序
            self.keys.append(key)
            self.keys.pop(index)
        elif len(self.hash) < self.capacity:
            self.hash[key] = value
            self.keys.append(key)
        else:
            try:
                # 删除一个又插入一个self.capacity保持不变
                self.hash.pop(self.keys[0])
                self.keys.pop(0)

                self.hash[key] = value
                self.keys.append(key)
            except Exception as e:
                print(e)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(10)
    cache.put(10, 13)
    cache.put(3, 17)
    cache.put(6, 11)
    cache.put(10, 5)
    cache.put(9, 10)

    print(cache.get(13))

    cache.put(2, 19)

    print(cache.get(2))
    print(cache.get(3))

    cache.put(5, 25)

    print(cache.get(1))

    print(cache.get(3))

    print(cache.get(4))

