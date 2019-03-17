# coding:utf-8


def quick_sort(alist,first,last):
    """快速排序"""
    if first >= last:
        return
    mid_val = alist[first]  # 先将参考点的值取出
    low,high = first,last
    while low<high:
        while low < high and alist[high] >= mid_val:
            high -= 1
        alist[low] = alist[high]    # 将右边小于参考值的值覆盖左边大于参考值的位置
        while low < high and alist[low]< mid_val:
            low += 1
        alist[high] = alist[low]    # 将左边大于参考值的值覆盖右边小于参考值的位置
    alist[low] = mid_val            # 将参考值覆盖参考点应该在的位置
    quick_sort(alist, first, low-1) # 将左边递归排序
    quick_sort(alist, low+1, last)  # 将右边递归排序

    
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(li,0,len(li)-1)
    print(li)
