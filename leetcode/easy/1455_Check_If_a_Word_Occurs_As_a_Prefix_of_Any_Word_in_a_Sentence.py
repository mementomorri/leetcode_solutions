class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split()
        for i in range(len(sentence_list)):
            if sentence_list[i].startswith(searchWord):
                return i + 1
        return -1
