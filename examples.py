

def ex3(x):
    l=len(str(x))
    count=0
    for i in range(l):
        y=x%10
        count+=y
        x=x//10
    return  count
s=ex3(136)
#print(s)
def ex4(x):
    temp=x
    l=len(str(x))
    count=0
    for i in range(l):
        y=x%10
        count+=y**3
        x=x//10
    if(count==temp):
        print("it is Armstrong")
    else:
        print("it is't Armstrong")
#ex4(153)
def ex5(s,t):
    for i in range(s,t):
        if(i%4!=0):
            if(i%9==0):
              print(i,end=',')
#ex5(1,100)
def ex6(x):
    if(x==1):
        return 1
    else:
        return x*ex6(x-1)
f=ex6(5)
#print(f)
def ex7(x,y):
    count=0
    if(x==1):
        return 1
    elif(y==1):
        return x
    else:
        return x*ex7(x,y-1)
e=ex7(2,4)
#print(e)
def ex8(x,y,z):
    if(x-y==z):
        print(x,'-',y,'=',z)
    elif(x+y==z):
         print(x,'+',y,'=',z)
    elif(x*y==z):
         print(x,'*',y,'=',z)
    elif(x**y==z):
           print(x,'**',y,'=',z)
    elif(x/y==z):
           print(x,'/',y,'=',z)
    elif(x//y==z):
           print(x,'//',y,'=',z)
    elif(x%y==z):
           print(x,'%',y,'=',z)
#ex8(2,3,6)
def ex9():
  x=input("enter the string")
  print(x.upper())
#ex9()
def ex12():

    x=input("enter string")
    y=input("enter number")
    p="ahmed"
    s=list(x)
    y=int(y)
    s[y]=''
    ss="".join(s)
    print(ss)
#ex12()
def ex13():
    string=input("Enter string:")
    if(string==string[::-1]):
      print("The string is a palindrome")
    else:
      print("The string isn't a palindrome")
#ex13()

def ex14():
    m=input("enter the start")
    n=input("enter the end")
    p=input("enter the postion")
    list=[]
    m=int(m)
    n=int(n)
    p=int(p)
    for i in range(m,n):
       d=input()
       d=int(d)
       list.append(d)
    list.pop(p)
    print(list)
   # a = array.array('i',(1 for i in range(0,10)))
    #print(a)

#ex14()

def ex15():
   s = input("Input a string")
   d=l=0
   for c in s:
     if c.isdigit():
         d=d+1
     elif c.isalpha():
         l=l+1
     else:
        pass
   print("Letters", l)
   print("Digits", d)

#ex15()

def ex17(x):
    list=[1,1]
    sum=0
    for i in range(0,x-2):
        sum=list[i]+list[i+1]
        list.append(sum)
    print(list)
#ex17(6)

def ex18(x):
    for i in range(1,12+1):
        print(i,"*",x,"=",i*x)


#ex18(6)
