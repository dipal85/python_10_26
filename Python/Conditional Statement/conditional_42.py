#42. Write a program to perform calculator operations using match case.

a = int(input("Num 1: "))
b = int(input("Num 2: "))
op = input("Op (+,-,*,/): ")
match op:
    case "+": print(f"Result: {a + b}")
    case "-": print(f"Result: {a - b}")
    case "*": print(f"Result: {a * b}")
    case "/": print(f"Result: {a / b}" if b != 0 else "Div by zero")
    case _: print("Invalid operator")