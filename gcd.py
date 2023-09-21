num=int(input("enter the number1:"))
num1=int(input("enter the number2:"))
if num1>num:
    temp=num1
    num1=num
    num=temp
    temp=int(temp)
gcd=1

for i in range(2,num//2):
    if num%i==0 and num1%i==0:
        gcd=gcd*i

        
print("gcd=",gcd)