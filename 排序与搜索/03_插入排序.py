# coding:utf-8

def insert_sort(alist): # 插入算法
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
    #return alist 本函数改变原列表，因此无需返回

def insert_sort_optimization(alist):    # 插入算法优化
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:                   # 因为插入的是有序序列，没有必要继续对比
                break
    #return alist 本函数改变原列表，因此无需返回

if __name__ == "__main__":
    L = [12,19,17,18,14,11,15,13,16]
    insert_sort_optimization(L)
    print(L)

