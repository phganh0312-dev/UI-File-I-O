class HashTable:

    def __init__(self, size=100):

        self.size = size

        self.table = []

        for _ in range(size):

            self.table.append([])

    def hash_function(self, key):

        return hash(key) % self.size

    def insert(self, key, value):

        index = self.hash_function(key)

        bucket = self.table[index]

        for pair in bucket:

            if pair[0] == key:

                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):

        index = self.hash_function(key)

        bucket = self.table[index]

        for pair in bucket:

            if pair[0] == key:

                return pair[1]

        return None

    def exists(self, key):

        return self.get(key) is not None

    def delete(self, key):

        index = self.hash_function(key)

        bucket = self.table[index]

        for i, pair in enumerate(bucket):

            if pair[0] == key:

                bucket.pop(i)
                return True

        return False
