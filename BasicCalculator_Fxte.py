# smart_calculator.py
import math
import sympy as sp

print("=== Basic Calculator_fxte ===")
print("Type 'exit' to quit.")

while True:
    expr = input("Enter calculation: ")
    if expr.lower() == "exit":
        print("Goodbye!")
        break
    
    try:
        expr = expr.replace("^", "**")
        if "!" in expr:
            n = int(expr.replace("!", ""))
            result = math.factorial(n)
        else:
            result = sp.sympify(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)