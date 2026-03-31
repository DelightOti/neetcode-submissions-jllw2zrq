class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Plan:
        start a pointer at first character
        start a pointer at end character

        while left <= right:

            temp = char at right
            right = left
            left = temp

            increment left
            decrement right
        """

        l = 0
        r = len(s) - 1

        while l < r:

            temp = s[r]
            s[r] = s[l]
            s[l] = temp

            l += 1
            r -= 1 

        