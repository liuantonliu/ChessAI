def partition(arr,left,right):
    pivot = arr[left]
    low = left+1
    high = right
    while low <= high:
        while arr[low] < pivot:
            low += 1
            if low == len(arr):
                break
        while arr[high] > pivot:
            high -= 1
            if high == -1:
                break
        if low <= high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
    temp = arr[left]
    arr[left] = arr[high]
    arr[high] = temp
    return high

def quicksort(arr,left,right):
    if left <= right:
        pivot = partition(arr,left,right)
        quicksort(arr,left,pivot-1)
        quicksort(arr,pivot+1,right)
    return True

# data = [5,1,3,7,9,2,4,6,8]
# print(data)
# quicksort(data,0,len(data)-1)
# print(data)

def hanoi(n,start,temp,final):
    if n>0:
        hanoi(n-1,start,final,temp)
        final.append(start.pop())
        hanoi(n-1,final,temp,start)
        print(start,temp,final)
        return True
    else:
        return True

# n = 3
# start = [1,2,3]
# temp = []
# final = []
# hanoi(n,start,temp,final)
# print("final",final)