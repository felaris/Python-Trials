#calculator
print("Type any Two numbers")

num1 = input("First Number : ")
num2 = input("Second Number : ")

print("************Print Choose an Operator************** ")

print("Press 1 , to select Adittion +")
print("Press 2 , to select subtraction _")
print("Press 3 , to select multiplication * ")
print("Press 4 , to select Division /")

operator = input(int("Press the number for the operator : "))


if operator == 1 :
        final = num1 + num2
        print(str("Answer :"+ final))
elif operator == 2:
        final = num1 - num2
        print(str("Answer :"+ final))
elif operator == 3:
        final = num1*num2
        print(str("Answer :"+ final))
elif operator == 4:
        final = num1/num2
        print(str("Answer :"+ final))
elif operator >=5:
        print("Please Type a correct number for the opertaor")
elif operator <=0:
        print(" Please Type a correct number for the  Opertaor ")










