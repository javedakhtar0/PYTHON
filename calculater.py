from ast import operator


num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operator=input("what do you want to do(+,-,*,/):")
if operator=="+":
    sum=int(num1+num2)
    print("addition of two numbers=",sum)
elif operator=="-":
    sub=int(num1-num2)
    print("subtraction of two numbers=",sub)
elif operator=="*":
    mul=int(num1*num2)
    print("multiplication of two numbers=",mul)
elif operator=="/":
    div=int(num1/num2)
    print("division of two number=",div)
else:
    print("sorry operator is not exist in list")
   
