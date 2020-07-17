#coding=utf-8
'''
author:@supercaizehua
----------------------
输入: 数组nums , 非负整数 k
k是旋转的步数
比如说 [1,2,3,4,5,6] k=2
第一次旋转[6,1,2,3,4,5]
第二次旋转[5,6,1,2,3,4]
输出旋转后的数组
其它限制:
O(1)空间, 原地处理
'''
from typing import List
'''
solution1: 暴力法
按照题目步骤, 旋转多次
时间O(nk)
空间O(1)
'''
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or k == 0: return
        size = len(nums)
        while k:
            target = nums[-1]
            for i in range(size):
                temp = nums[i]
                nums[i] = target
                target = temp
            k -= 1

class Solution1_2: #pythonic
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or k == 0: return
        for i in range(k):
            nums.insert(0, nums.pop())


'''
solution2: 使用额外数组 不符合题意
原本数组里index为i的元素, 放到 (i + k) % size 的位置, 最后把新数组拷贝到原数组中
'''

'''
solution3: 三次反转
1反转所有元素
2反正前k个元素
3反转剩下的元素
顺序也可以是321or231 但是要注意到底是前k个还是后k个
时间O(n)
空间O(1)
'''
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or k == 0: return
        size = len(nums)
        k %= size
        def reverse(index_l, index_r):
            while index_l < index_r:
                nums[index_l], nums[index_r] = nums[index_r], nums[index_l]
                index_l += 1
                index_r -= 1
        # reverse all 
        reverse(0, size - 1)
        reverse(0, k-1)
        reverse(k, size - 1)


'''
solution4: 原地翻转
https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode/
题解中的环状替换
一次遍历
时间O(n)
空间O(1)
'''
class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or k == 0: return
        size = len(nums)
        k %= size
        count = start = 0
        while count < size:
            current = start
            prev = nums[start]

            while True:
                nex = (current + k) % size
                nums[nex], prev = prev, nums[nex]
                current = nex
                count += 1
                if start == current: break
            
            start += 1

if __name__ == "__main__":
    test_nums = [1,2,3,4,5,6,7]
    k = 3
    a = Solution4()
    a.rotate(test_nums, k)
