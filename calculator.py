"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter your equation>")
    tokens = input_string.split(" ")

    
    if "q" in tokens:
        print ("Exit the calculator")
        break
    
    else:
        operator = tokens[0]
        num1 = float(tokens[1])
        result= None
    
        if len(tokens) < 3:
            num2= "0"
        else:
            num2 = float(tokens[2])

        if operator == "+":
            result= add(num1, num2)
        
        elif operator == "-":
            result= subtract(num1, num2)
        
        elif operator == "*":
            result= multiply(num1, num2)

        elif operator == "/":
            result= divide(num1, num2)
        
        elif operator == "square":
            result= square(num1)
    
        elif operator == "cube": 
            result= cube(num1)
        
        elif operator == "pow":
            result= power(num1, num2)
        
        elif operator == "mod":
            result= mod(num1, num2)

        print(result)