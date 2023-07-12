def simplecalucation(a,b,s):  #a,b are variables, s is for selection
    if(s==1):
        print(a+b)
    elif(s==2):
        print(a-b)
    elif(s==3):
        print(a*b)
    elif(s==4):
        print(a/b)
    else:
        print("enter the valid no")
        pass
a=int(input("enter the fist value :"))
b=int(input("enter the second value :"))
print("1:addition,2:subtraction,3:multiplication,4:division")
s=int(input("select the calculation :"))
simplecalucation(a,b,s)
