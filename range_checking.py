m,n =map(int,input("enter range:").split())
num=""
print("enter . to terminate:")
while(num !="."):
    num=(input("enter value to check:"))
    if(num == "."):
        break;
    if(int(num) < m or int(num) >n):
        print("invalid")
    else:
        print("valid")
