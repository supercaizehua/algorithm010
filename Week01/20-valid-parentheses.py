#coding=utf-8
'''
author: @supercaizehua
data: 2020-7-2 05:06:52
---------------------------------------------------------------
理解题意:
输入字符串 只包含 3种括号对
输出是否有效
有效条件
- 左括号必须用相同类型右括号闭合
- 左括号必须以正确的顺序闭合    [(]) 就不是有效的字符串
'''

'''
1.暴力法
循环,每次匹配到一对有效括号就替换成空字符
时间O(n^2) 空间O(1) 为什么是O(n^2)
'''
class Solution1:
    def isValid(self, s: str) -> bool:
        L = len(s)
        L1 = L
        if L % 2 != 0: return False
        while L:
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
            L = len(s)    
            if L == L1: return False
            L1 = L
        return True

class Solution1_1:#国际版大神 pythonic 天下第一!
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
        return not len(s)
'''
2.栈
- 遇到左括号入栈,遇到右括号就弹出对应栈顶左括号
- 建立hash表, key左括号, value右括号, 用于查询是否对应 O(1)时间

边界问题
- stack为空的时候, stack.pop()报错, 可以想链表添一个dummy头一样, 可以给stack一个初值, 同时在hash表中说明k-v
- 以左括号结尾, 遍历完整个s后, stack还有未出栈的左括号, 最后需要判断一下

时间O(n), 空间O(n)
'''
class Solution2:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}', '[':']', '(':')', '0':'0'}
        stack = ['0']
        for i in s:
            if i in dic: 
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        return stack.pop() == '0'