class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        '''
        Get the count of each letter in tasks

        use counts to make the MaxHeap and heapify it

        make an empty queue
        create time variable and set it to zero

        while either maxheap exists or queue exists:
            time= time+1
            if maxheap is not empty:
                current pop the greatest from maxheap
                incrementt the current by 1 becasue we used it oncre

                if current!=0:
                    push (current, time+n) into queue
                
            if queue is not empty and queuetime=time:
                take front of queue so deque
                push whatever it is into heap
        
        return time
        '''

        
        count = Counter(tasks)

        maxHeap=[]
        for c in count.values():
            heapq.heappush(maxHeap,-c)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                current = heapq.heappop(maxHeap)
                current += 1        # we used one instance

                if current != 0:
                    queue.append((current, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time