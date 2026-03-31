class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        length of nums1 = m + n
        length of muns2 = n

        Plan:
        
        ptr2 = 0 (nums2)

        ptr1 = len(nums1) - 1

        while right > right - n:
            set value at right to value at num2[ptr2]

            increment ptr2
            decrement ptr1

        run nums.sort
        """

        ptr1 = len(nums1) - 1
        ptr2 = 0
        
        N = len(nums1) - len(nums2) - 1

        while ptr1 > N:

            nums1[ptr1] = nums2[ptr2]

            ptr2 += 1
            ptr1 -= 1
        
        nums1.sort()        