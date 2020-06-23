#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-23 14:26:38
---------------------------------------------------------------
理解题意:
输入: n 台阶数(正整数)
每次只能爬 1 级或 2 级台阶
输出: 不同的爬法数
'''

'''
没有思路的时候怎么办? 先尝试暴力法, 如果暴力法不行, 就先列一些最简单的情况, 从中寻找最近重复子问题
层数  方法
1    1                       f(1) = 1
2    1+1 2                   f(2) = 2
3    1 1 1   1 2  2 1        f(3) = 3 = f(2) + f(1)
4?   从3层+1     从2层+2      f(4) = f(3) + f(2)
5?   从4 + 1     从3+ 2       f(5) = f(4) + f(3)
...
n                            f(n) = f(n-1) + f(n-2)
----------------------------------------------------------------------------
所以最后题目就变成了求 f(n) = f(n-1) + f(n-2)    f(1) = 1, f(2) = 2
'''

'''
解法1 
递归  时间复杂度很大
改良方式就是 递归+缓存  以空间来换时间
'''
class Solution1_1:
    def climbStairs(self, n: int) -> int:        
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution1_2:#数组(列表)作为缓存
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        cache = [0 for i in range(n)]
        cache[0], cache[1] = 1, 2
        return self.get_ans(n-1, cache)

    def get_ans(self, n, cache):
        if cache[n] == 0: 
            cache[n] = self.get_ans(n-1, cache) + self.get_ans(n-2, cache)
        return cache[n]

class Solution1_3:#字典作为缓存
    def __init__(self):
        self.dict = {1:1, 2:2}
    
    def climbStairs(self, n: int) -> int:
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]

'''
解法2
开辟一个数组
用一个循环直接计算
时间复杂度O(n) 空间O(n)
'''
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        a = [0 for i in range(n)]
        a[0], a[1] = 1, 2
        for i in range(2, n):
            a[i] = a[i-1] + a[i-2]
        return a[n-1]

'''
解法3
解法2的优化, 即不需要开辟数组, 直接存3个值即可
时间O(n) 空间O(1)
'''
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        f1, f2 = 1, 2
        for i in range(1, n-1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

#国际版牛逼写法
# def climbStairs(self, n):
#     a = b = 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

#国际版python较为全面的解答
# https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down)


if __name__ == "__main__":
    test_n = 10
    a = Solution1_3()
    ans = a.climbStairs(test_n)
    print(ans)

