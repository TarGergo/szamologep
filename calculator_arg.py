import sys

import secret_logic

print(f"{sys.argv}, {len(sys.argv)}")

def printusageandexit():
    print("Incorrect syntax")
    exit(-1)

def process_one_row(row):
    parts = row.split()
    if len(parts) != 3:
        printusageandexit()

    if not secret_logic.is_numeric(parts[0]):
        printusageandexit()
    op1 = int(parts[0])

    if not secret_logic.is_supported(parts[1]):
        printusageandexit()
    operator = parts[1]

    if not secret_logic.is_numeric(parts[2]):
        printusageandexit()
    op2 = int(parts[2])

    return op1, operator, op2

def getinputs():
    for row in sys.stdin:
        process_one_row(row)

op11, operator1, op22 = getinputs()
result = secret_logic.calculate(op11, operator1, op22)
print(f"Results: {result}")
exit(0)