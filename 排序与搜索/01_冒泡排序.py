# coding:utf-8

''' 冒泡排序 '''
def bubble_sort(a_list):      
    n = len(a_list)
    for i in range(n, 0, -1): # 对i个数进行一轮冒泡，每次冒泡最大的数沉到最后
        for j in range(i-1):  # 进行i-1次比较，将数大的交换到后面
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]
    #return a_list  本函数改变原列表，因此无需返回
   
        
def bubble_sort_optimization(a_list):
    n = len(a_list)
    for i in range(n, 0, -1): # 对i个数进行一轮冒泡，每次冒泡最大的数沉到最后
        flag = 1    # 序列有序标志位，
        for j in range(i-1):  # 进行i-1次比较，将数大的交换到后面
            if a_list[j] > a_list[j+1]:
                flag = 0
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]
        if flag:    # 如果序列本身有序，则无需继续冒泡
            break
    #return a_list  本函数改变原列表，因此无需返回
        
if __name__ == "__main__":
    
    L = [12,19,17,18,14,11,15,13,16]
    #L = [1,2,3,4,5,6,7,8,10,9]  # 前面有序，而后面无序

    bubble_sort_optimization(L)
    print(L)

    #L = [11, 22,11,12, 22, 25, 34, 64, 90]
