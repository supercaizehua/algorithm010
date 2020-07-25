import heapq
'''
heapq有两种方式创建堆
一种, 使用一个空列表, 然后用heapq.push()把值加入列表中
第二种, 使用heap.heapify(list)转换列表成为堆结构
'''
if __name__ == "__main__":
    nums = [1,2,3,4,51,2,1,132]
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    print(heap[0])
    print([heapq.heappop(nums) for _ in range(len(nums))])


    nums = [1,2,3,4,51,2,1,132]
    heapq.heapify(nums)
    print([heapq.heappop(nums) for _ in range(len(nums))])
