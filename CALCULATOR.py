print("----CALCULATOR----")
print(" SELECT AN OPERATION")
print(" 1. ADD")
print(" 2. SUBTRACT")
print(" 3. MULITPLY")
print(" 4. DIVIDE")

def add(x1,x2):
    return x1 + x2

def sub(x1,x2):
    return x1 - x2

def mul(x1,x2):
    return x1 * x2

def div(x1,x2):
    return x1 // x2

op = int(input(" ENTER OPERATION OF YOUR CHOICE (1,2,3,4) : "))

if op == 1 or op == 2 or op == 3 or op == 4:
    operand1 = int(input(" ENTER 1ST OPERAND : "))
    operand2 = int(input(" ENTER 2ND OPERAND : "))

    if op == 1:
        print("ANSWER : ", add(operand1, operand2))

    if op == 2:
        print("ANSWER : ", sub(operand1, operand2))

    if op == 3:
        print("ANSWER : ", mul(operand1, operand2))

    if op == 4:
        print("ANSWER : ", div(operand1, operand2))

else:
    print("INVALID INPUT")


