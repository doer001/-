# coding:utf-8
'''
1，将一个列表平均分为左右两个列表，
2，对左右两个列表分别采用归并排序
3，将排好序的两个列表进行合并

'''
def merge(left,right):
    result = []
    len_left,len_right = len(left),len(right)
    i,j = 0,0
    while(i<len_left and j<len_right):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if(i==len_left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    return result

def merge_sort(List):
    n = len(List)
    if(n<2):
        return List
    middle = n//2
    left = List[:middle]
    right = List[middle:]
    left =merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
    

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)

