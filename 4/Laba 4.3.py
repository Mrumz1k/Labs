from enum import Enum

class Operation(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

def calculate(first_number, second_number, operation: Operation):
    if operation == Operation.ADD:
        result = first_number + second_number
    elif operation == Operation.SUB:
        result = first_number - second_number
    elif operation == Operation.MUL:
        result = first_number * second_number
    elif operation == Operation.DIV:
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Ошибка: деление на ноль"
    else:
        result = "Неизвестная операция"

    return first_number, second_number, operation.value, result

a, b, op, res = calculate(10, 5, Operation.MUL)
print(f"{a} {op} {b} = {res}")