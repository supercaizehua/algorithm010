#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-22 18:34:45
'''

'''
理解题意:
返回数组下标
只有唯一解
同一个元素不能重复使用
解不存在返回什么?
'''

from typing import List
'''
1.暴力法, 两个循环,  时间复杂度O(n^2), 空间复杂度O(1)
'''
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth = len(nums)
        for i in range(lenth-1):
            for j in range(i+1, lenth):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
            

'''
2.哈希(用字典代替哈希表) 空间O(n)
'''
class Solution2_1: #两遍哈希表 时间O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            dic[num] = index
        for i,num in enumerate(nums):
            if target - num in dic:
                j = dic[target - num]
                if i != j:
                    return [i,j]

class Solution2_2: #一遍哈希表, 遍历的同时判断, 时间O(n), 比上面快一点点
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

                
'''
3.排序+双指针 时间O(nlogn) 排序的时间较大 空间O(n)
1 先将下标和数字存入一个字典
2 排序
3 双指针寻找目标
4 找回下标
'''
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # copy a list
        temp = nums.copy()
        # sort list
        temp = sorted(temp)
        # find two num
        r, l = 0, len(nums) - 1
        while r < l:
            _sum = temp[r] + temp[l]
            if _sum > target:
                l -= 1
            elif _sum < target:
                r += 1
            else:
                break
        i = nums.index(temp[r])
        nums.pop(i)
        j = nums.index(temp[l])
        if j >= i:   #如果j>=i, 则说明 j 在 i 后面, 由于 pop 出了一个元素, 所以 index 需要 +1
            j += 1
        return [i,j]











if __name__ == "__main__":
    test_nums = [1,2,3,4,5,6]
    test_target = 11
    a = Solution1()
    ans = a.twoSum(test_nums, test_target)
    print(ans)


