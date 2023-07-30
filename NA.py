# Created By Mr NAIB
logo = """   
\033[0;32m$$\   $$\  $$$$$$\  
$$$\  $$ |$$  __$$\ 
$$$$\ $$ |$$ /  $$ |
$$ $$\$$ |$$$$$$$$ |
$$ \$$$$ |$$  __$$ |
$$ |\$$$ |$$ |  $$ |
$$ | \$$ |$$ |  $$ |
\__|  \__|\__|  \__|    
 \033[0;31m Tool Created By √ Mr Naib   
 \033[1;33m first Tool Thanks √ GOD                                                                                          
"""

# Calculator function
def calculator():
    print(logo)
    while True:
        try:
            num1 = float(input("\033[1;33m the first number: "))
            operator = input("\033[0;32m an operator (+, -, *, /): ")
            num2 = float(input("\033[0;31m the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("\033[0;31m operator. Please try again.")
                continue

            print(f"\033[0;32m: {result}")
            break

        except ValueError:
            print("\033[1;33m input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("\033[0;31m divide by zero. Please try again.")

# Call the calculator function
calculator()
