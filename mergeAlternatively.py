from typing import List
def mergeAlternately(word1: str, word2: str) -> str:
        word = ""
        i=0
        minlength = min(len(word1), len(word2))
        while i < minlength:
            word = word + word1[i] + word2[i]
            i += 1
        if len(word1) < len(word2):
            word = word + word2[i:len(word2)]
        else: 
            word = word + word1[i:len(word1)]
        print(word)
        return word
        
mergeAlternately("abc","pqr")
mergeAlternately("ab","pqrs")
mergeAlternately("abcd","pq")