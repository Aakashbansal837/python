b,n,m = map(int,input().split())
keyboard = [int(x) for x in input().split()]
usb = [int(x) for x in input().split()]
val = -1
for i in keyboard:
    for j in usb:
        num = i+j
        if num<=b:
            if num > val:
                val = i+j
print(val)
