'''
author:@supercaizehua
---------------------
输入 有序整数数组 nums1 nums2
将 nums2 合并到 nums1
要保证nums1的有序性
m, n 是两个数组的元素个数
原地修改nums1
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass


'''
solution1: 合并后排序
时间O((n+m)log(n+m))
空间O(1)
'''

'''
solution2:双指针/从前往后
额外拷贝一个nums1
时间O(m+n)
空间O(m)
'''
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m].copy()
        i = j = index = 0
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[index] = temp[i]
                i += 1
            else:
                nums1[index] = nums2[j]
                j += 1
            index += 1
        
        if i == m:
            nums1[i + j:] = nums2[j:]
        else:
            nums1[i + j:] = temp[i:]

        nums1 = nums1[:m+n]

'''
solution3: 双指针/从后往前
优化方法2, 合理利用m,n这个信息, 从后往前遍历
时间O(m+n)
空间O(1)
'''
class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = m-1, n-1
        tail = m + n -1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1
            tail -= 1

        if j >= 0:#当nums2还没遍历完的时候, 说明nums2剩下的元素要比nums1的元素都要小
            nums1[:j] = nums2[:j]



        