def searching(arr,e):
    while True:
        mid = len(arr)//2
        left=arr[:mid];right=arr[mid:]
        if e<arr[mid]:
            arr=left
        elif e>arr[mid]:
            arr=right
        else:
            return "Found"
        if len(arr)==0:
            return "Not found"

    

x=list(map(int,input("Enter array elements\n").split()))
y=int(input("What you want to search\n"))
print("Number {} ".format(searching(x,y)))
