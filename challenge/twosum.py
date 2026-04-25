class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Cách 3: lưu vào một dictionary (key, value) = (number, index)
        seen = {}
        for i, val in enumerate(nums):
            second_val = target - val 
            if second_val in seen:
                return [i, seen[second_val]]
            else:
                seen[val] = i
        
        # Cách 2: Sử dụng 2 con trỏ L và R trong một list phải được sắp xếp trước đấy
        # nums_with_index = []
        # n = len(nums)
        # for i in range(n):
        #     nums_with_index.append([nums[i], i])
        #     nums_with_index.sort()

        # L= 0
        # R = n - 1 
        # while L < R:
        #     current_sum = nums_with_index[L][0] + nums_with_index[R][0]
        #     if current_sum < target:
        #         L += 1
        #     elif current_sum > target:
        #         R -= 1 
        #     else:
        #         return [nums_with_index[L][1], nums_with_index[R][1]]
        
        # Cách 1: Sử dụng Brute Force lặp qua từng vị trí trong list 2 vòng lặp lồng nhau để lấy 2 số 
        # n = len(nums)
        # # Vòng lặp thứ nhất để chọn số thứ nhất
        # for i in range(n):
        #     # Vòng lặp thứ hai để chọn số thứ hai (bắt đầu từ i + 1)
        #     for j in range(i + 1, n):
        #         # Kiểm tra xem tổng có bằng target không
        #         if nums[i] + nums[j] == target:
        #             return [i, j] # Trả về vị trí (index) i và j
                
s = Solution()
result = s.twoSum([3, 2, 4, 15], 6)
print(result)