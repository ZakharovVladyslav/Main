'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''

import os

os.system("cls")

def arithmetic(num1, num2, action):
    if action == "+":
        num1 += num2
        
    elif action == "-":
        num1 -= num2
    
    elif action == "/":
        num1 /= num2
    
    elif action == "*":
        num1 *= num2
        
    else:
        print("You've entered wrong option")
    
    return num1

# main section 

print("What do you want to choose? (choose from the list below)")
print("> Calculator - calc\n>Check all results - file")
choice = str(input("Choice:"))

if choice == "calc":
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    action = str(input("Enter action: "))
    count = 1

    file = open("results.txt", "a")

    result = arithmetic(num1, num2, action)
    print("Result: ", result)
    file.write("\n")
    file.write(f"Result {count}: {result}\n")    

    answer = str(input("Want to continue? (yes / no): "))
    count += 1

    if answer == "yes":
        while answer != "no":
            num1 = int(input("Enter num1: "))
            num2 = int(input("Enter num2: "))
            action = str(input("Enter action: "))
                
            result = arithmetic(num1, num2, action)
            print("Result: ", result)  
            file.write(f"Result {count}: {result}\n")
                
            answer = str(input("Want to continue? (yes / no): "))
            count += 1
            
    file.close()
            
elif choice == "file":
    file = open("results.txt", "r")
    
    print(file.read())
    
    file.close()
    
else:
    print("Wrong variant")
    os._exit()