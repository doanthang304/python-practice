class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse_number = 0 
        og_number = x
        while x > 0:
            last_digit = x % 10
            reverse_number = (reverse_number * 10) + last_digit   
            x = x // 10
        if reverse_number == og_number:
            print("True")
        else:
            print("False")

Solution().isPalindrome(121)