from collections import deque
d = deque()
for i in range(int(input())):
    tmp = input().split()
    if tmp[0] == "append":
        d.append(int(tmp[1]))
    elif tmp[0] == "appendleft":
        d.appendleft(int(tmp[1]))
    elif tmp[0] == "pop":
        d.pop()
    elif tmp[0] == "popleft":
        d.popleft()
print(*d,sep=" ")
