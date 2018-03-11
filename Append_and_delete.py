def appendAndDelete(s, t, k):
    n1,n2 =0,0;
    len1 =len(s);len2 = len(t);
    for i in range(len1):
        if(s[i] == t[i]):
            n1+=1;n2+=1
        else:
            break
    n1 = len1-n1
    n2 = len2-n2
    r =n1+n2
    if(r == k):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
