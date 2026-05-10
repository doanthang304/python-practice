# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x) # Biến x thành giá trị luôn dương

        result = 0
        
        if result > 2*31 -1 or result < -2*31:
            return 0
        while x > 0:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10
        return result * sign  

        
print(Solution().reverse(-123))