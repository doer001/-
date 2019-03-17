# coding:utf-8

 
''' 选择排序 '''
def select_sort(alist):
    n = len(alist)
    for i in range(n-1):  # 挑出第i小的数放到第i个位置,挑了n-1轮
        min_index = i
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:  # 如果后面有更小的，则交换
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist
        

def select_sort_optimization(alist):
    n = len(alist)
    for i in range(n//2):  # 挑出第i小的数放到第i个位置,挑了n-1轮
        min_index,max_index = i,n-1-i
        for j in range(i+1,n-1-i):
            if alist[j] < alist[min_index]:
                min_index = j
            if alist[j] > alist[max_index]:
                max_index = j
        if min_index != i:  # 如果后面有更小的，则交换
            alist[i], alist[min_index] = alist[min_index], alist[i]
        if max_index != n-1-i:  # 如果前面有更大的，则交换
            alist[n-1-i], alist[max_index] = alist[max_index], alist[n-1-i]
    if n%2==1:
        if alist[n//2-1]>alist[n//2]:
            alist[n//2-1],alist[n//2] = alist[n//2],alist[n//2-1]
        if alist[n//2]>alist[n//2+1]:
            alist[n//2+1],alist[n//2] = alist[n//2],alist[n//2+1]
    #return alist  本函数改变原列表，因此无需返回
    
    
if __name__ == '__main__':
    L = [12,19,17,18,14,11,15,13,16]
    select_sort_optimization(L)
    print(L)
    #L = [11, 22,11,12, 22, 25, 34, 64, 90]
