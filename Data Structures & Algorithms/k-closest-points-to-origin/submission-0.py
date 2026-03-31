class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        make a list and call it heap

        for x and y in points:
            calculate the distance
            push it into the heap 
        
        make a result list
        iterate thru the heap while less than k
            pop value from heap and add it to resule
        return result
        '''

        heap=[]

        for x,y in points:
            dist= x*x + y*y
            heapq.heappush(heap, (dist,[x,y]))
        
        result=[]
        for x in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result