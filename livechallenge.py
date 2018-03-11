if __name__ == '__main__':
    n = int(input())
    val=input().split()
    for i in range(len(val)):
        val[i]=int(val[i])
    abc=tuple(val)
    h = hash(abc)
    print(h)
