# -*- coding: utf-8 -*-


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq as hp
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        heap = []
        for key in hashmap:
            hp.heappush(heap,(hashmap[key],key))
            if len(heap) > k:
                hp.heappop(heap)
        rec = []
        for i in range(len(heap)):
            rec.append(heap[i][1])
        return rec