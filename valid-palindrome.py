# https://leetcode.com/problems/valid-palindrome/submissions/1256066493/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.casefold()
        start = 0
        end = len(s) - 1

        while(start < end):
            while(not s[start].isalnum() and start < end):
                start+=1
            while(not s[end].isalnum() and end > start):
                end-=1
            if(start > end or s[start] != s[end]):
                return False
            start+=1
            end-=1
        return True