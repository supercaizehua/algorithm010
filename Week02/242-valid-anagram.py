'''
author:@supercaizehua
------------------------
字母异位词:
ant 和 tan是字母异位词
rat 和 car 不是字母异位词
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass

'''
s1: 排序, 然后比较排序后的是否相同
时间 O(nlogn)
空间 O(1)
'''
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

'''
s2: 哈希表计数
两个哈希表
时间O(n)
空间O(n)
'''
import collections
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

'''
s3:哈希表计数
1个哈希表
s中出现的字母+1
t中出现的字母-1
时间O(n)
空间O(n)
'''
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        c = collections.Counter(s)
        for i in t:
            if i in c:
                c[i] -= 1
                if c[i] == 0: del c[i]
            else:
                return False
        return True if not c else False