class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        '''
        sort the array
        start from the back

        iterate thru the array
        if x==y:
            remove both from array
        if x<y:
            change y=y-x
            remove x
        at the end return value in list
        else return 0 if list is empty
        '''

        stones.sort()

        while len(stones)>1:
            x=len(stones)-1
            y=x-1
            if stones[x]==stones[y]:
                stones.pop(x)
                stones.pop(y)
            else:
                stones[y]=stones[x]-stones[y]
                stones.pop(x)
            
            stones.sort()
            print(stones)


        return stones[0] if stones else 0
