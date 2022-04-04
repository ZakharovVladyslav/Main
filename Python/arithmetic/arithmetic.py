'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''

import os

os.system("cls")

def arithmetic(num1, num2, action):
    if (action == "+"):
        num1 += num2
        
    elif (action == "-"):
        num1 -= num2
    
    elif (action == "/"):
        num1 /= num2
    
    elif (action == "*"):
        num1 *= num2
        
    else:
        print("You've entered wrong option")
    
    return num1
    

#def save_results(result, num_of_operations):
def save_results(result):
    file = open("results.txt", "w")
    
    #file.write(f"Operation {num_of_operations}, result: {result}\n")
    file.write(str(result))
    
    file.close()

# main section 
    
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
action = str(input("Enter action: "))

result = arithmetic(num1, num2, action)
print("Result: ", result)    
save_results(result)

answer = str(input("Want to continue? (yes / no): "))
while (answer != "no"):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    action = str(input("Enter action: "))
        
    result = arithmetic(num1, num2, action)
    print("Result: ", result)    
    save_results(result)
        
    answer = str(input("Want to continue? (yes / no): "))
        
    if (answer == "yes"):
        os._exit()
        
    else:
        continue