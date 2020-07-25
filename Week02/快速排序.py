'''
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：

挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
'''

def partition(arr, low, high):
    pivot = low
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[high] = pivot
    return high

def partition2(nums, low, high):
    pivot = nums[low]
    i = low
    for j in range(i+1, high + 1):
        if nums[j] < pivot:
            nums[i+1],nums[j] = nums[j],nums[i+1]
            i+= 1
    nums[low], nums[i] = nums[i], nums[low]
    return i





'''
arr[]  对象
low    起始索引
high   终止索引
'''
def quickSort(arr, low, high):
    if low < high:
        pi = partition2(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)







if __name__ == "__main__":
    a = [11, 20, 28, 9, 74, 9, 67, 21, 25, 64, 66, 31, 75, 99, 64, 53, 50, 98, 47, 67]
    quickSort(a, 0, len(a)-1)
    print(a)



