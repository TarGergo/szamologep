def ask():
    print("Calculator app. Please write down these: ")

    print("1.operand(integer): ")
     text = input()
     while not text.isnumeric():
       print("bad input again")
       text = input()
     operand1 = int(text)

     print("Operator(+,-,*,/)")
     text = input()
     while text not in ('+', '-', '*', '/'):
          print("bad input (again)")
          text = input()
     loperator = text

     print("2.operand(integer)")
     text = input()
     while not text.isnumeric():
          print("bad input again")
          text = input()
     operand2 = int(text)

     return operand1, loperator, operand2


def calculate(operand1, poperator, operand2):
     rv = 0
     if poperator == '+':
         rv = operand1 + operand2
     elif poperator == '-':
         rv = operand1 - operand2
     elif poperator == '*':
         rv = operand1 * operand2
     elif poperator == '/':
         rv = operand1 / operand2
     return rv

op1, operator, op2 = ask()
result = calculate(op1, operator, op2)
print(f"Results: {result}")
exit(0)