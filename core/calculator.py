from decorators import cache_decorator

def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    operationsDict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '**': lambda x, y: x ** y
    }
    return operationsDict[operation](a, b)


if __name__ == '__main__':
    aString = input('Введите первое число: ')
    while not aString.isdigit():
        print('Это не число')
        aString = input('Введите первое число: ')
    a = int(aString)

    bString = input('Введите второе число: ')
    while not bString.isdigit():
        print('Это не число')
        bString = input('Введите второе число: ')
    b = int(bString)

    operationsList = ['+', '-', '/', '*', '**']
    operation = input('Введите операцию: ')
    while not operation in operationsList:
        print('Операция ' + operation + ' не поддерживается')
        operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))
    
    calculator = cache_decorator(calculator)
    print('Результат с кешированием: ', calculator(a, b, operation))
