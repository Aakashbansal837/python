def ptrn(n):
    print("**"," "*n,"**"*n)
    print("**"," "*n,"**"*n)
    for i in range(n):
        print("**"," "*n,"**")
    print("**"*(n*2))
    print("**"*(n*2))
    for i in range(n):
        print("  "*(n-1),"**"," "*(n),"**")
    print("**"*n," "*(n-1),"**")
    print("**"*n," "*(n-1),"**")

if __name__ == "__main__":
    n=int(input("Enter odd number greater than 5:"))
    if(n>=5 and n%2 !=0):
        ptrn(n)
    else:
        print("enter correct value:")
