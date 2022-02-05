
num1 = int(input("Enter 1st Number:\n"))
opt = input("Enter Your operator Pleas\n")
num2 = int(input("Enter 2nd Number:"))

if num1 == 55 and num2 == 3 and opt =='*':
    print("555")
elif num1==56 and num2== 9 and opt=='+':
    print("The number is : 77")
elif num1== 56 and num2== 6 and opt=='/':
    print("The solution is : 4")
elif opt=='/':
    print(num1/num2)
elif opt == '+':
    print(num1+num2)
elif opt == '-':
    print(num1 - num2)
elif opt == '%':
    print(num1 % num2)
elif opt == '*':
    print(num1 * num2)
else:
    print("invalid Input! please try again")
