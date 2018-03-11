print("enter variables for calculator:")
z='y'
while(z=="y" or z=="Y"):
  if(z=="y" or z=="Y"):  
    a=input("A=")
    a=int(a)
    b=input("B=")
    b=int(b)

    print("Enter arithmatic Opration")
    c=input()
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="/"):
        print(a/b)
    elif(c=="*"):
        print(a*b)
    else:
        print("wrong choise")
    print("Continue Y or N")
    z=input()
  elif(z=="n" or z=="N"):
       exit()
  else:
        print("wrong Choice but exit")
        exit()
