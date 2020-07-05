#coding=utf-8
'''
author: @supercaizehua
data: 2020-7-2 18:07:50
'''

'''
理解题意:
输入n个非负整数，求能勾勒出来的最大矩形
'''
'''
1.1 暴力解法, 双循环遍历
'''
class Solution1_2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L = len(heights)
        res = heights[0] if L else 0
        
        for i in range(L):
            H = heights[i]
            for j in range(i, L):
                width = j - i + 1
                H = min(H, heights[j])
                res = max(res, H * width)
        return res

'''
1.2 暴力解法 中心扩展:
枚举以每个柱形为高度的最大面积
固定中间,遍历左右边界
时间O(n^2)?
空间O(1)
'''
class Solution1_2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L = len(heights)
        res = 0
        for i in range(L):
            left = right = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1
            while right < L-1 and heights[right + 1] >= cur_height:
                right += 1

            res = max(res, (right - left + 1) * cur_height)

        return res


class Solution1_2_1: # 进一步优化中心扩展法
    def largestRectangleArea(self, heights: List[int]) -> int:







'''
2.栈
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
时间
空间
'''
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        stack = []

        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 0 is not None:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)

        return res


'''
加入哨兵优化代码
'''
class Solution2_1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res




            

