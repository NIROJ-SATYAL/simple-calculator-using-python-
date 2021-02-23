def sum(a,b):
    s=a+b
    return print(s)


a=int(input("enter tthe value of a"))
b=int(input("enter the value of b"))
sum(a,b)

def diff(a,b):
    d=a-b
    return print(d)

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
diff(a,b)

def mul(a,b):
    m=a*b
    return print(m)

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
mul(a,b)

def div(a,b):
    if(b== 0):
         return  print("this is not possible ")
    else:
        D=a/b
        return print(D)

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
div(a,b)


