#coding = utf-8
'''
author: @suepercaizehua
----------------------------
理解题意:
输入: 数组nums , 滑动窗口k
返回: 数组, 元素为滑动窗口中的最大值
其它条件:
1<= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''

'''
1.暴力法
遍历每个滑动窗口，找到每个窗口的最大值。一共有 N - k + 1 个滑动窗口，每个有 k 个元素，
时间O（nk）
'''
class Solution1:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums
        return [max(nums[i:i + k]) for i in range(n - k + 1)] 


'''
2.双向队列
处理前k个元素， 初始化双向队列
遍历整个数组，同时清理双向队列
- 只保留当前滑动窗口中有的元素的索引
- 移除比当前元素小的所有元素
将当前元素添加到队列中
将deque【0】添加到输出中
返回
时间O（n） 空间O（n）
'''
from collections import deque
class Solution2:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        deq = deque()
        ans = []
        for i,n in enumerate(nums):
            while deq and nums[deq[-1]] < n:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k: #最左边出去
                deq.popleft()
            if i >= k - 1: # i < k-1 的时候, 我们正在初始化双端队列
                ans.append(nums[deq[0]])
        return ans


'''
3.dp
将数组分割成k个元素的块
