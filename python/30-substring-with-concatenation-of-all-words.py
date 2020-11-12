from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        word_counter, substring_word_counter = {}, {}
        result = []
        wordsize = len(words[0])
        concatsize = wordsize*len(words)

        for word in words:
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1

        for i in range(len(s)-concatsize+1):
            substring = s[i:i+concatsize]
            for j in range(len(words)):
                subword = substring[wordsize*j:wordsize*(j+1)]
                if subword not in substring_word_counter:
                    substring_word_counter[subword] = 1
                else:
                    substring_word_counter[subword] += 1
            
            valid_word = (word_counter == substring_word_counter)
            if valid_word: result.append(i)
            
            substring_word_counter = {}

        return result
