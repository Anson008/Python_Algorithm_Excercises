import string


class Solution(object):
    def ladder_length(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        if end_word not in word_list:
            return 0
        ans = 1
        frontier = [begin_word]
        used = set(frontier)
        while frontier:
            next = []
            for word in frontier:
                for p in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:p] + c + word[p + 1:]
                        if new_word == end_word:
                            return ans + 1
                        if new_word in word_list and new_word not in used:
                            used.add(new_word)
                            next.append(new_word)
            frontier = next
            ans += 1
        return 0


    
