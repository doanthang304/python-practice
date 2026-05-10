#Greedy: Thuat toan tham lam/ Mapping
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ''
        for i in range(len(numbers)):
            count = (num // numbers[i])
            result += romans[i] * count
            num %= numbers[i]
        return result
    
print(Solution().intToRoman(58))
