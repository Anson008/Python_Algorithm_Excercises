class TrieTreeNode:
    def __init__(self):
        self.children = [None] * 26
        # indicate if it is the end of a word
        self.is_end = False
        # indicate how many words used this node
        self.count = 0


class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode()

    def search(self, word):
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.children[index] is None:
                return False
            else:
                curr = curr.children[index]
        return curr.is_end

    def add(self, word):
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieTreeNode()
            curr.count += 1
            curr = curr.children[index]
        curr.is_end = True

    def delete(self, word):
        self._delete_helper(self.root, word, 0)

    def _delete_helper(self, curr, word, index):
        if index == len(word):
            curr.is_end = False
            return None
        i = ord(word[index]) - ord('a')
        self._delete_helper(curr.children[i], word, index + 1)
        if curr.children[i].count == 0:
            curr.children[i] = None
        curr.count -= 1


if __name__ == "__main__":
    trie_tree = TrieTree()
    trie_tree.add("abc")
    trie_tree.add("abd")
    trie_tree.delete("abd")
    print(trie_tree.search("abc"))
