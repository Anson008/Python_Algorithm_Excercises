class Solution:
    @staticmethod
    def is_all_unique(word):
        hash_set = set()
        for c in word:
            if c in hash_set:
                return False
            hash_set.add(c)
        return True

    