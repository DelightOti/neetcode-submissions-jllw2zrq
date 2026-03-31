class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        since python defaults a minHeap
        
        convert all stones to negative values
        heapify the list   // creates a min heap that acts like a max heap

        while heap has more than one stone:
            y = pop from heap and negate it   // largest stone
            x = pop from heap and negate it   // second largest stone

            if y != x:
                push -(y - x) into heap

        if heap is empty:
            return 0
        else:
            return negate top of heap
        '''

        for x in range(len(stones)):
            stones[x]=-stones[x]
        heapq.heapify(stones)

        while len(stones)>1:
            y=-(heapq.heappop(stones))
            x=-(heapq.heappop(stones))

            if y!=x:
                heapq.heappush(stones,-(y-x))
        
        if not stones:
            return 0
        else:
            return -stones[0]