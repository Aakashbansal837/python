cube = lambda x: x**3
def fibonacci(n):
    initiallist = []
    for i in range(n):
        if i < 2:
            initiallist += [i]          
        else:
            initiallist += [initiallist[-1] + initiallist[-2]]
    return initiallist

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
