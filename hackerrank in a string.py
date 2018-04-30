for _ in range(int(input())):
    s=list(input())
    st="hackerrank"
    j=0
    for i in s:
        if j<10:
            if i ==st[j]:
                j+=1
    if j == 10:
        print("YES")
    else:
        print("NO")
    
