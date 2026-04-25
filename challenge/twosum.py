class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        # Vòng lặp thứ nhất để chọn số thứ nhất
        for i in range(n):
            # Vòng lặp thứ hai để chọn số thứ hai (bắt đầu từ i + 1)
            for j in range(i + 1, n):
                # Kiểm tra xem tổng có bằng target không
                if nums[i] + nums[j] == target:
                    return [i, j] # Trả về vị trí (index) i và j
                
s = Solution()
result = s.twoSum([3, 2, 4, 15], 6)
print(result)