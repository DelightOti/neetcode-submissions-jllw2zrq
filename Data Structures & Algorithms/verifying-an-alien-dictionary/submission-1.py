class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # first differing char
        # if word a is prefix, word b comes after

        orderindex = {}

        # create a hashmap for easy lookups
        for i, c in enumerate(order):
            orderindex[c] = i
        
        # iterate over the words array comparing the adjacents
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            # if w2 is a prefix for w1
            for j in range(len(w1)):
                if j == len(w2):
                    return False
            
                if w2[j] != w1[j]:
                    if orderindex[w1[j]] > orderindex[w2[j]]:
                        return False
                    break
        return True
