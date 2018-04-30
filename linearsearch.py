def searching(arr,e):
    for i in range(len(arr)):
        if arr[i]==e:
            return arr.index(e)+1
    return "Not found"

x=list(map(int,input("Enter array elements\n").split()))
y=int(input("What you want to search\n"))
print("The position is {} ".format(searching(x,y)))
