print("Basic Calculator")
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
math_op=input("Choose one of these operations:(+,-,/,*): ")

if math_op=='+':
    result=num1 + num2
    print("Result:",result)
elif math_op=='-':
    result=num1 - num2
    print("Result:",result)
elif math_op=='*':
    result=num1 * num2
    print("Result:",result)
elif math_op=='/':
    if num2 !=0:
        result=num1 / num2
        print("Result:",result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Error: Invalid operation")



