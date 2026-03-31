class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        iterate over array
        left equal i
        vtotarget=target-left
        res=[]

        right=left+1
        while right<len(array):
            if right = vtotarget and right value > left value:
                add left, right to the list
                break
        return list
        '''

        res=[]
        for left in range(len(numbers)):
            vtf=target-numbers[left]
            right=left+1
            while right<len(numbers):
                if numbers[right] == vtf and numbers[right]>numbers[left]:
                    res.append(left+1)
                    res.append(right+1)
                    break
                right+=1
        return res


