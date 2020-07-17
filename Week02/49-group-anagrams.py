'''
author:@supercaizehua
-------------------------
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
输入 list[str]
输出 分好组的列表, 将异位词放进一个列表
例子: 
    输入["eat", "tea", "tan", "ate", "nat", "bat"]
    输出[
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
        ]

其它条件: 输入都小写, 不考虑答案的顺序
'''
from typing import List
import collections

'''
so1:哈希表
维护一个哈希表
key: tuple(排好序的元素)
value: [元素]

时间O(NKlogK)
空间O(NK)
'''
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for string in strs:
            ans[tuple(sorted(string))].append(string)
        return ans.values

class Solution1_1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        
        return list(dic.values())    

class Solution1_2: # 大神代码
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return list(dic.values())

'''
so2: 按字母计数分类
'''
class Solution2_1: #通过数组手动去计数
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

class Solution2_2: #通过collections.counter手动去计数
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            c = collections.Counter(sorted(s))
            ans[tuple(c.items())].append(s)
        return list(ans.values())