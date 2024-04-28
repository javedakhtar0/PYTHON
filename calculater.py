from ast import operator


num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operator=input("what do you want to do(+,-,*,/):")
if operator=="+":
    sum=int(num1+num2)
    print("addision of",num1, " and ",num2, " = ",sum)
elif operator=="-":
    sub=int(num1-num2)
    print("subtraction of",num1, " and ",num2, " = ",sub)
elif operator=="*":
    mul=int(num1*num2)
    print("multiplication of",num1, " and ",num2, " = ",mul)
elif operator=="/":
    div=int(num1/num2)
    print("division of",num1, " and ",num2, " = ",div)
else:
    print("sorry operator is not exist in list")
   
