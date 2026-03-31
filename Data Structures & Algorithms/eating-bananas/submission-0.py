class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        '''
        find the max value in the array

        left=0
        right=len(newarray)-1
        rate=0
        iterate over a new array from 1 to the maxvalue
        while left<=right:
            do binary search such that
            mid=(left+right)//2

            iterate over the original piles array from left to right
                rate+=piles[i]//mid
            if rate<h:
                right=mid-1
            if rate>h:
                left=mid+1
            if res<h and value>res:
                res=value
        return res
        '''

        left=1
        right=max(piles)
        answer=right

        while left<=right:
            mid=(left+right)//2
            hours=0

            for i in piles:
                hours+= math.ceil(i/mid)
            if hours<=h:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer