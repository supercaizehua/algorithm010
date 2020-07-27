'''
author:@supercaizehua
----------------------
输入 nums  target
找4个元素和为target
返回 列表
列表元素为4元组, 且所有元素不重复
'''
from typing import List
'''
暴力解法就不写了
solution1: 双指针
'''
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        size = len(nums)
        if not nums or size < 4: return ans
        nums.sort()

        for a in range(size - 3):
            if a > 0 and nums[a] == nums[a-1]: continue
            current_min = nums[a] + nums[a+1] + nums[a+2] + nums[a+3]
            if current_min > target: break
            current_max = nums[a] + nums[-1] + nums[-2] + nums[-3]
            if current_max < target: continue

            for b in range(a+1, size - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                current_min = nums[a] + nums[b] + nums[b+1] + nums[b + 2]
                if current_min > target: break
                current_max = nums[a] + nums[b] + nums[-1] + nums[-2]
                if current_max < target: continue

                c, d = b+1, size-1
                while c < d:
                    sum_ = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum_ > target:
                        d -= 1
                    elif sum_ < target:
                        c += 1
                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c<d and nums[c] == nums[c - 1]:
                            c += 1
                        d -= 1
                        while c<d and nums[d] == nums[d + 1]:
                            d -= 1
        return ans



'''
solution2
能不能把解法1转化成递归？
'''
class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        self.Nsum(nums, target, 4, [], ans)
        return ans

    def Nsum(self, nums, target, N,  ans_, ans):
        size = len(nums)
        if size < N or N < 2: return []
        if target < nums[0] * N or target > nums[-1] * N: return []

        if N == 2:
            l, r = 0, size - 1
            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ == target:
                    ans.append(ans_ + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum_ > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        else:
            for i in range(size - N + 1):
                if i > 0 and nums[i] == nums[i - 1]: continue
                self.Nsum(nums[i+1:], target-nums[i], N-1, ans_+[nums[i]], ans)
        return


        
        
        
        
        
        
        
        

