def selectionsort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                
arr=list(map(int,input().split()))
print("Before sorting")
print(arr)
selectionsort(arr)
print("After sorting")
print(arr)

