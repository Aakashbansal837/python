n,jump = map(int,input().split())
arr = [int(x) for x in input().split()]
energy = 100
pos = 0
while pos < n:
    if arr[pos] == 1:
        energy-=3
    else:
        energy-=1
    pos+=jump
print(energy)
    
    
