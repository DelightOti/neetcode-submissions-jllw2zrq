class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Plan:
        sort s
        sort t
        if sorted_s = sorted_t:
            return True
        return False

        make a dictionary
        iterate over s
            store thr values of s in the dictionary with their count
        iterave over t
            store the valeus of t in the dictionary with their conut
        check is the two dictionairies are the same
            return True
        return False
        '''

        s_dict={}
        t_dict={}

        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i]=1
        for i in t:
            if i in t_dict:
                t_dict[i]+=1
            else:
                t_dict[i]=1
        if s_dict == t_dict:
            return True
        else:
            return False
        