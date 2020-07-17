#coding=utf-8
'''
author: @supercaizehua
------------------------
https://leetcode-cn.com/problems/trapping-rain-water/
'''

'''
solution1: 暴力法 (超时了)
直接按问题描述进行, 对于数组中的每个元素, 找出下雨水之后能到达的最高位置
最高位置 = 两边最大高度的较小值减去当前高度的值
时间 O(n^2) 每个元素都需要向左向右扫描
空间 O(1)
'''
class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans, size = 0, len(height)
        for i in range(size):
            max_left, max_right = 0, 0
            j = i 
            while j >= 0:
                max_left = max(max_left, height[j])
                j -= 1
            k = i
            while k < size:
                max_right = max(max_right, height[k])
                k += 1
            ans += min(max_left, max_right) - height[i]
        return ans


'''
solution2: DP
如何优化暴力法?
我们为了找到最大值, 每次都要向左向右去扫描, 但是实际上我们可以提前存储这个值.
- 找到 i 到 最左端最高的高度 max_left
- 找到 i 到 最右端最高的高度 max_right
- 扫描数组并更新答案
    同时累加 min(max_left[i], max_right[i]) - height[i]

时间复杂度 O(n)  
    两次遍历 2* O(n)
    更新ans 1 O(n)
空间复杂度 O(n)
    开辟了两个数组空间
'''
class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans, size = 0, len(height)
        max_left = [0] * size
        max_right = max_left.copy()
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, size):
            max_left[i] = max(height[i], max_left[i-1])
        i = size - 2
        while i >= 0:
            max_right[i] = max(height[i], max_right[i+1])
            i -= 1
        for i in range(size):
            ans += min(max_left[i], max_right[i]) - height[i]
        return ans


'''
solution3: stack
这道题应用栈的思路有点类似于84题
使用栈来跟踪可能储水的最大的条形
如果当前的块<= 栈顶, 那么就入栈, 即: 当前的条形块被栈顶的块界定了
如果当前的块> 栈顶, 那么意思就是当前的块是栈顶块的另一个边界, 此时弹出栈顶元素并累加
时间 O(n)
    单次遍历
空间 O(n) 栈最多占用O(n)
'''
class Solution3:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans = current = 0
        stack = [] # stack 存储的是index
        size = len(height)
        
        while current < size:
            # 当前的块 > 栈顶
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack: break
                distance = current - stack[-1] - 1
                water_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * water_height
            stack.append(current)
            current += 1
        return ans

'''
so4:双指针
如果一端有更高的块, 水的高度由另一端决定
由此可以推断,如果整个数组中存在一个最大的块, 那么这个块左侧的水, 由块左侧的最大值决定, 右侧的水由右侧的最大值决定
如果存在多个相同的最大块, 任取一个, 同样符合这个规律
时间 O(n) 一次遍历
空间 O(1)
             top
              __
            _/  \       __
     __    /     \     /  \
_   /  \__/       \___/    \     __
 \_/                        \___/
'''
class Solution4:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0 
        ans = 0
        while left <= right:
            if left_max < right_max:
                ans += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                ans += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return ans