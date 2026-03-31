class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Plan:

        create a dictionary to store s letters and count
        create a dictionary to store t letters and count

        iterate over dictionary s:
            if letter at dict[s].values()!= same letter at dict(t).values:
                return False
        return True
        '''
        if len(s)!=len(t):
            return False

        dict_s={}
        dict_t={}

        for i in s:
            if i in dict_s:
                dict_s[i]+=1
            else:
                dict_s[i]=1
        
        for i in t:
            if i in dict_t:
                dict_t[i]+=1
            else:
                dict_t[i]=1
        
        return dict_s==dict_t
