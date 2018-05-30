n,m = map(int,input().split())
arr = [int(x) for x in input().split()]
bill = int(input())


total = (sum(arr[:m]+arr[m+1:]))/2
if total == bill:
    print("Bon Appetit")
else:
    print(bill-total)
