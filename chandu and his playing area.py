import sys
 
T = int(sys.stdin.readline().replace("\n", ""))
 
Counter = 1
while Counter <= T:
 
    Straw = int(sys.stdin.readline().replace("\n", ""))
 
    Side = Straw // 4
    Remainder = Straw % 4
 
    if Remainder == 0:
        Side1 = Side
        Side2 = Side
    elif Remainder == 1:
        Side1 = Side
        Side2 = Side
    elif Remainder == 2:
        Side1 = Side
        Side2 = Side + 1
    elif Remainder == 3:
        Side1 = Side
        Side2 = Side + 1
 
    Product = Side1 * Side2
 
    sys.stdout.write(str(Product) + "\n")
 
    Counter += 1
