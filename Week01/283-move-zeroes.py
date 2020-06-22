#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-22 13:31:34
'''
from typing import List

# 解法1: 直接交换非零元素和零元素位置  一次循环  时间复杂度 O(n) 空间复杂度 O(1)
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # current 0 index
        j = 0 
        for i in range(j, len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# 解法2: 两次循环 计算0的数量, 第一次非零元素往左挪, 第二次把末尾置零 时间复杂度O(n) 空间O(1)
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        for i in range(j, len(nums)):
            nums[i] = 0

# 解法3: 开一个新数组 不符合题意, 时间复杂度O(n), 空间复杂度O(n)
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = []
        for num in nums:
            if num != 0:
                new.append(num)
        for i in range(len(new), len(nums)):
            new.append(0)
        return new



if __name__ == "__main__":
    test_list = [0,0,1,2,3,4]
    a = Solution3()
    ans = a.moveZeroes(test_list)
    # print(ans)
    print(test_list)