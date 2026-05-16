expr = [2, "+", 4, "*", 6, "-", 8]

result = expr[0]

for i in range(1, len(expr), 2):
    op = expr[i]
    num = expr[i + 2]

    if op == "+":
        result += num
    
    elif op == "-":
        result -= num

    elif op == "*":
        result *=num
    
print(result)
    

