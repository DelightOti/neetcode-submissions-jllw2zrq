class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        '''
        start a pointer at word1
        start a pointer at word2
        create a new empty string

        while word1 and word2 exist:
           append char from word1 to empty string
           append char from word2 to empty string

           increment word1 ptr
           increment word2 ptr

        add word1 or word2 remains to the string
        return string 
        '''

        ptr1 = 0
        ptr2 = 0
        string = []

        while ptr1 < len(word1) and ptr2 < len(word2):
            string.append(word1[ptr1])
            string.append(word2[ptr2])

            ptr1 += 1
            ptr2 += 1

        if ptr1 < len(word1):
            string.append(word1[ptr1:len(word1)])
        else:
            string.append(word2[ptr2:len(word2)])
        
        result = "".join(string)

        return result

