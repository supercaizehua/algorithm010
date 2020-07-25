'''
author:@supercaizehua
---------------------
输入 数组 找出最小的k个数

0 <= k <= arr.length <= 1w
0 <= arr[i] <= 1w

'''



'''
直接暴力
时间O(NlogN)
'''
class Solution1:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k] if 0 < k <= len(arr) else []

'''
快排
快排O(NlogN), 在本题中直接通过快排排好第k小的数

目标最小的k个数, 假设经过一次partition操作, 枢纽元素下标m, 说明左侧的m个元素是最小的m个数
此时有3种情况
k=m, 直接返回结果
k<m, 我们要的结果一定在左侧, 继续左侧patition
k>m, 左侧m个数符合结果, 还需要在右侧寻找 k-m 个最小的数, 对右侧partition
空间O(1)
时间O(n), 最坏O(n^2)
'''
class Solution2:
    def getLeastNumbers(self, arr, k):
        if k >= len(arr): return arr
        if k == 0 or not arr: return []

        return self.quickSelect(arr, 0, len(arr)-1, k)

    def quickSelect(self, nums, start_index, end_index, k):
        low, high = start_index, end_index
        pivot_index = self.partition(nums, low, high)
        '''
        例如pivot_index = 4, 说明pivot左侧有4个数比它小0,1,2,3  
        k = 4
        因此输出[:k]
        '''
        if pivot_index == k:
            return nums[:k]
        elif pivot_index > k:
            return self.quickSelect(nums, low, pivot_index-1, k)
        else:
            return self.quickSelect(nums, pivot_index+1, high, k)
    
    def partition(self, nums, low, high):
        pivot = nums[low]
        while low < high: 
            while low<high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low



'''
堆
'''
class Solution3:
    def getLeastNumbers(self, arr, k):
        if k == 0 or not arr: return []
        if len(arr) <= k: return arr
        
        import heapq
        ans = []
        heapq.heapify(arr)
        for i in range(k):
            ans.append(heapq.heappop(arr))
        return ans



'''
数据范围有限时: 计数排序
'''
class Solution4:
    def getLeastNumbers(self, arr, k):
