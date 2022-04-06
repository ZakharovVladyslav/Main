'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''

import sys
import os
import os.path

os.system("cls")

def arithmetic(nums, action):
    if action == "+":
        res = 0
        for i in range(len(nums)):
            res += nums[i]

    elif action == "-":
        for i in range(len(nums) - 1):
            nums[0] -= nums[i + 1]
        res = nums[0]
    
    elif action == "/":
        for i in range(len(nums) - 1):
            nums[0] /= nums[i + 1]
        res = nums[0]
    
    elif action == "*":
        for i in range(len(nums) - 1):
            nums[0] *= nums[i + 1]
        res = nums[0]
        
    else:
        print("You've entered wrong option")
        sys.exit()

    return res


# main section 


while True:

    _str = ""

    print("\n" + _str.center(27, "-") + "\nWhat do you want to choose? (choose from the list below)\n----")
    print("> Calculator - calc\n> Check all results - file\n> Exit - exit\n> Recall programm - rec\n> Delete results fils - del")
    choice = str(input("Choice: "))
    os.system("cls")
    print("\n" + _str.center(27, "-"))

    if choice == "calc":
        
        num_of_nums = int(input("Enter number of numbers: "))
        nums = []
        for i in range(num_of_nums):
            i += 1
            num = int(input(f"Number {i}: "))
            nums.append(num)  
            
        action = str(input("Enter action: "))
        count = 1

        file = open("results.txt", "a")

        result = arithmetic(nums, action)
        print("-----------")
        print("Result: ", result)
        file.write(f"Result {count}: {result}\n")    
        file.write("\n")

        print("\n" + _str.center(30, "-"))
        answer = str(input("Want to continue? (yes / no): "))
        print(_str.center(30, "-") + "\n")
        
        count += 1

        if answer == "yes":
            while answer != "no":
                 
                num_of_nums = int(input("Enter number of numbers: "))
                nums = []
                for i in range(num_of_nums):
                    i += 1
                    num = int(input(f"Number {i}: "))
                    nums.append(num)  
            
                action = str(input("Enter action: (+ | - | * | / "))
                    
                result = arithmetic(nums, action)
                print("-----------")
                print("Result: ", result)  
                file.write(f"Result {count}: {result}\n")
                file.write("\n")
                
                print(_str.center(30, "-"))    
                answer = str(input("\nWant to continue? (yes / no): "))
                print(_str.center(30, "-" + "\n"))
                count += 1
                
        file.close()
                
    elif choice == "file":
        
        if os.path.exists("results.txt"):
        
            file = open("results.txt", "r")
            
            print("-----------\n" + file.read() + "-----------")
            
            file.close()
        else:
            print("Such file doesn't exist. Do you want to create a file?\n" + _str.center(25, "-"))
            
            file_choice = str(input("Create a file? (yes / no)\n\nChoice: "))
            
            if file_choice == "yes":
                print(_str.center(22, "-") + "\nFile has been created!\n")
                
                file = open("results.txt", "w")
                file.write("Results:\n")
                file.close()
            
            elif file_choice == "no":
                continue
            
            else:
                sys.exit()
            
    elif choice == "del":
        if os.path.exists("results.txt"):
            os.remove("results.txt")
            print("----\nFile has been deleted\n----")
        else:
            print("Such file does not exist...")
            del_choice = str(input("----\nWant to create file? (yes / no)\nChoice: "))
            if del_choice == "yes":
                file = open("results.txt", "w")
                print("----\nFile has been created!\n----")
                file.write("Results:\n")
                file.close()
        
    elif choice == "exit":
        sys.exit()
        
    elif choice == "rec":
        os.system("exit")
        os.system("python .\\arithmetic.py")
        
    else:
        sys.exit()