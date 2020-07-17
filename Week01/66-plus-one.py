'''
author:@supercaizehua
-----------------------
输入: 整数组成的非空数组表示的非负整数, 就是[1,2,3]表示 123
且出了0以为, 所有数不会以0开头 不会出现[0,1,2]这样的东西
数组中,每个元素范围0-9
输出: 数组

难点是如何处理进位?
'''

'''
solution1: 按数学正常进位
最坏情况O(n) 最快O(1), 平均 O(n)
空间O(1)
'''
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return [1]
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            i -= 1
            if i == -1:
                digits = [1] + digits
                break
            digits[i] += 1

        return digits

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return [1]
        for i in range(1, len(digits) + 1):
            if digits[-i] < 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0
        return [1] + digits