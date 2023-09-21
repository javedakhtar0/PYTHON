def emp():
    
    temp=1
    num=int(input("enter the number:"))
    for i in range(1,num+1):
        temp=temp*i
        print(i,end="*")
    print("\b =",temp)

emp()
