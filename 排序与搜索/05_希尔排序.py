#coding:utf-8
'''
希尔排序涉及排序远离其他的元素。对给定列表的大型子列表进行排序，
并继续缩小列表的大小，直到所有元素都被排序。 
'''

def shell_sort(alist):
    n = len(alist)
    gap = n// 2
    while gap > 0:
        for j in range(gap, n): # 实质上是步长为gap的插入算法
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap = gap//2
    #return alist  本函数改变原列表，因此无需返回


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)

