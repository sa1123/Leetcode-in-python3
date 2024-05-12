# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<0:
            neg = True
            x*=-1
        ans = 0
        while(x):
            ans = ans*10 + x%10
            x//=10
        if(ans > 2**31 - 1):
            return 0
        if(neg):
            return -1*ans
        else:
            return ans