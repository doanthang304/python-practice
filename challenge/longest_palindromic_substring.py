class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""   
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1

            return s[left + 1:right] 

        for i in range(len(s)):
            le = expand(i,i)
            chan = expand(i,i + 1)
            if len(le) > len(result):
                result = le

            if len(chan) > len(result):
                result = chan

        return result
        
s = Solution()
result = s.longestPalindrome("abbd")
print(result)