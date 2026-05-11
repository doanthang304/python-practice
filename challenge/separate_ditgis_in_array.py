#Separate the Digits in an Array
from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        return result
    
s = Solution()
print(s.separateDigits([21,34,67]))

C:\Users\ADMIN\Coding\python_practice\challenge\separate_ditgis_in_array.py