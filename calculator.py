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
        for i in range(len(inputs)-1):
            inputs[i+1] # do whatevs

        #for i in (len(inputs)-1):
            #input_number = int(inputs[i])

        # i1 = int(inputs[1])
        # i2 = int(inputs[2])
        # i3 
        # i4


            if inputs[0] == '+':
                for input_number: 
                    add(input_number)
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