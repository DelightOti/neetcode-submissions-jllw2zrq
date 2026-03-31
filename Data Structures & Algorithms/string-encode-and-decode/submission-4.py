class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        Plan:
        if the input string is empty
            return empty list
        for every string in strs
            compute the length of each string and save it in an array sizes
        take all the numbers in the array and then add it to an a string separating each
        by commas and then a # and then the rest of the words in strs
        ''' 

        if not strs:
            return ""
        
        sizes=[]
        for s in strs:
            sizes.append(str(len(s)))

        res=[]
        for i in range(len(sizes)):
            res.append(sizes[i]+",")
        
        # mark the start of the string
        res.append("#")

        for s in strs:
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        '''
        Plan:
        make a sizes array
        make a res array

        if string is empty:
            return ""
        string not empty so
        

        sizes=[]
        # at the end of this loop index will be at #
        iterate over string until u get to #
            if string is a number
                add it to sizes
            if string is a comma 
                continue
            increment i
        
        res=[]
        for size in sizes:
            # find a way to append from (i to i+size)
            res.append(s[])
            i+=size
        return res
        '''

        if not s:
            return []
        
        i = 0
        num = ""
        sizes = []
        
        while s[i] != "#":
            if s[i] == ",":
                sizes.append(int(num))
                num = ""
            else:
                num += s[i]
            i += 1
        
        # store last number if no comma before '#'
        if num:
            sizes.append(int(num))

        # skip '#'
        i += 1
        
        res = []
        for size in sizes:
            word = s[i:i+size]
            res.append(word)
            i += size

        return res
