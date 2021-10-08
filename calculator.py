import secret_logic

def ask():
    print("Calculator app. Please write down these: ")

    print("1.operand(integer): ")
     text = input()
     while not secret_logic.is_numeric(text):
       print("bad input again")
       text = input()
     operand1 = int(text)

     print("Operator(+,-,*,/)")
     text = input()
     while not secret_logic.is_supported(text):
          print("bad input (again)")
          text = input()
     loperator = text

     print("2.operand(integer)")
     text = input()
     while not secret_logic.is_numeric(text):
          print("bad input again")
          text = input()
     operand2 = int(text)

     return operand1, loperator, operand2



op1, operator, op2 = ask()
result = secret_logic.calculate(op1, operator, op2)
print(f"Results: {result}")
exit(0)