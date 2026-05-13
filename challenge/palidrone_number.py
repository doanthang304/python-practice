class Solution_1:
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
            print("Solution_1: True")

class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_number = 0
        while x > reverse_number:
            last_digit = x % 10
            reverse_number = (reverse_number * 10) + last_digit
            x = x // 10
        if x == reverse_number or x == reverse_number // 10:
            print("Solution_2: True")

Solution_1().isPalindrome(121)
Solution_2().isPalindrome(121)
