# https://leetcode.com/problems/palindrome-number/submissions/1255544424/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        temp = x
        reverse = 0
        while(temp):
            reverse = reverse*10 + temp%10
            temp//=10
        return(reverse == x)