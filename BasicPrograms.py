import time

print("----- WELCOME to BASIC PYTHON PROGRAMMING -----")

name = str(input("Enter your name: "))
print ("Hello ", name, "Welcome back to Python")

for i in name:
    print(i)
    
def main_menu():
    while True:
        print ("---CHOOSE AN ACTIVITY---")
        print ("press 1 for AGE GUESSER")
        print ("press 2 for CALCULATOR")
        print ("press 3 for MONEY CONVERTER")
        print ("press 4 for ORGANIZE ITEMS")
        print ("press 0 to  EXIT")
        act = int(input("Choose an activity: "))  
        
        if act ==0:
            print("Thank you for using the program!")
            break
        elif act ==1:
            age_guesser()
        elif act ==2:
            calculator()
        elif act ==3:
            money_converter()
        elif act ==4:
            organize_items()
        else:
            print("Choose only between 1-4")
  

def age_guesser():
    
    print ("---AGE GUESSER---")
    age = int(input("Enter age: "))
    if age <= 10:
        print (str(age) + " yrs old is a baby")
    elif age <= 12:
        print (str(age) + " yrs old is a toddler")
    elif age <= 17:
        print (str(age) + " yrs old is a teenager")

    elif age >= 18:
        print (str(age) + " yrs old is an adult")
        
    time.sleep(3)
   

def calculator():
    
    print ("---CALCULATOR---")
    try:
        n1 = int(input("Enter number 1: "))
        n2 = int(input("Enter number 2: "))
    except ValueError:
        print("Only input numbers!")
        time.sleep(2)
        return calculator()
    
    add = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    div = n1 / n2
    print("---RESULT---")
    print("Addition: " + str(add))
    print("Subtraction: " + str(sub))
    print("Multiplication: " + str(mult))
    print("Division: "+ str(div))
    
    time.sleep(3)


def money_converter():
    print ("---MONEY CONVERTER---")
    pesos = int(input("Enter money in peso: "))
    print(" ")
    print("---CHOOSE to CONVERT to---")
    try:
        convert = int(input("(1.Dollars) (2. Yen) (3. Euro) (4. Rupees) --> "))
    except ValueError:
        print("Input the designated number!")
        return money_converter()
    
    if convert == 1:
        exchange = 0.0176
        sign = "$"
    elif convert == 2:
        exchange = 2.66
        sign = "¥"
    elif convert == 3:
        exchange = 0.0163
        sign = "€"
    elif convert == 4:
        exchange = 1.
        sign = "₹"
    else:
        print("Choose only between 1-4")
        return money_converter
    
    equals = pesos * exchange
    
    print(" ")
    print( pesos , "₱ ---> ", equals, sign)

    
    time.sleep(3)


def organize_items():
    print ("---ORGANIZE ITEMS---")
    items = input("Input Items: ").split()
    items.sort()
    print(" ")
    for item in items:
         print(item)
         
    time.sleep(3)



main_menu()