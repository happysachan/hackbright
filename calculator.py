from arithmetic import add, subtract, multiply, divide, square, power, mod

while True:
    calc = raw_input("> ")
    inputs = calc.split(" ")
    len(inputs)
    print inputs

    i1 = int(inputs[1])
    i2 = int(inputs[2])

    if inputs[0] == '+':
        print add(i1,i2)
    if inputs[0] == '-':
        print subtract(i1,i2)
    if inputs[0] == '*':
        print multiply(i1,i2)   
    if inputs[0] == '/':
        print divide(i1,i2)   
    if inputs[0] == 'square':
        print square(i1)   
    if inputs[0] == 'pow':
        print power(i1,i2)
    if inputs[0] == '%':
        print mod(i1,i2)      