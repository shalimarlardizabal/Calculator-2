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
        num1 = tokens[1]
        result= None
    
        if len(tokens) < 3:
            num2= "0"
        else:
            num2 = tokens[2]

        if operator == "+":
            result= add(float(num1), float(num2))
        
        elif operator == "-":
            result= subtract(float(num1), float(num2))
        
        elif operator == "*":
            result= multiply(float(num1), float(num2))

        elif operator == "/":
            result= divide(float(num1), float(num2))
        
        elif operator == "square":
            result= square(float(num1))
    
        elif operator == "cube": 
            result= cube(float(num1))
        
        elif operator == "pow":
            result= power(float(num1), float(num2))
        
        elif operator == "mod":
            result= mod(float(num1), float(num2))

        print(result)