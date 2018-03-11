def insort(n, arr):
    if arr == sorted(arr):
        return 0
    count=0;ar =arr
    for i in range(1,n):
        if ar != sorted(arr):
            ar = sorted(arr[:i])
            print(ar)
            count+=1
        else:
            break
    print(arr)
    return count

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insort(n, arr)
        print(result)
