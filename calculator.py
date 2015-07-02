from arithmetic import *

while True:
    calc = raw_input("> ")
    inputs = calc.split(" ")
    #print len(inputs)

    if len(inputs) == 2:
        i1 = int(inputs[1])

        if inputs[0] == 'square':
            print square(i1)  
        if inputs[0] == 'cube':
            print cube(i1)
    else:
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
        if inputs[0] == 'pow':
            print power(i1,i2)
        if inputs[0] == '%':
            print mod(i1,i2)      