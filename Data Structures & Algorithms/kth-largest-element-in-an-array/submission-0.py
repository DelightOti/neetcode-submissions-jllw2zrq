class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        '''
        make a list call it heap

        iterate over nums
            for each value build the heap by calling heappush bc that automatically heapifys it
            but store the negative value of it 

        pop heap k times to get value
        '''

        heap=[]

        for i in range(len(nums)):
            heapq.heappush(heap, -(nums[i]))
        
        for _ in range(k):
            x=-(heapq.heappop(heap))
        
        return x
