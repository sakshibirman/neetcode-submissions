class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        a=0
        b=len(clean)-1
        while a<b:
            if clean[a]!=clean[b]:
                return False
            else:
                a=a+1
                b=b-1
        return True
                




        


