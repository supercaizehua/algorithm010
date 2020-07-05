# 二分查找

## 前提

1. 单调性
2. 有界
3. 能够通过索引访问(index)

## 代码模板

部分条件需要根据实际情况微调

```python
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # target found
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

