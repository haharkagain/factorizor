import sys
import math

def checkPrime():
    number = int(input("number: "))
    factor = 2
    if (number / factor != int(number / factor)):
        factor = 3
        while (factor <= (int(math.sqrt(number))) and number / factor != int(number / factor)):
            factor += 2
    if (number / factor == int(number / factor)):
        print("composite")
    else:
        print("prime")

def factors():
    number = int(input("number: "))
    factor = 0
    factors = []
    while (factor <= int(math.sqrt(number))):
        factor += 1
        if (number / factor == int(number / factor)):
            factors.append(factor)
            factors.append(int(number / factor))
    i = 0 
    while (i < len(factors)):
        print("{} * {}".format(factors[i], factors[i+1]))
        i += 2

def factorize():
    number = int(input("number: "))
    factor = 3
    factors = []
    loop = 1
    exponent = 1
    exponentForm = []
    while (loop == 1):
        if (number / 2 == int(number / 2)):
            factors.append(2)
            number = number / 2
        else:
            while (factor <= (int(math.sqrt(number))) and number / factor != int(number / factor)):
                factor += 2
            if (number / factor != int(number / factor)):
                if (number != 1):
                    factors.append(int(number))
                loop = 0
            else:
                factors.append(factor)
                number = number / factor
                factor == 3
    for i in range (len(factors)):
        if (i + 1 < len(factors)):
            if (factors[i] == factors[i+1]):
                exponent += 1
            else:
                exponentForm.append("{} ^ {}".format(factors[i], exponent))
                exponent = 1
        else:
            exponentForm.append("{} ^ {}".format(factors[i], exponent))
            exponent = 1
    for i in range (len(exponentForm)):
        print("{} ".format(exponentForm[i]), end="")
        if (i + 1 < len(exponentForm)):
            print("* ", end="")

def modFactorize():
    number = int(input("number: "))
    factor = 3
    factors = []
    loop = 1
    exponent = 1
    exponentForm = []
    while (loop == 1):
        if (number % 2 == 0):
            factors.append(2)
            number = number / 2
        else:
            while (factor <= (int(math.sqrt(number))) and number % factor != 0):
                factor += 2
            if (number % factor != 0):
                if (number != 1):
                    factors.append(int(number))
                loop = 0
            else:
                factors.append(factor)
                number = number / factor
                factor == 3
    for i in range (len(factors)):
        if (i + 1 < len(factors)):
            if (factors[i] == factors[i+1]):
                exponent += 1
            else:
                exponentForm.append("{} ^ {}".format(factors[i], exponent))
                exponent = 1
        else:
            exponentForm.append("{} ^ {}".format(factors[i], exponent))
            exponent = 1
    for i in range (len(exponentForm)):
        print("{} ".format(exponentForm[i]), end="")
        if (i + 1 < len(exponentForm)):
            print("* ", end="")

def modCheckPrime():
    number = int(input("number: "))
    factor = 2
    if (number % factor != 0):
        factor = 3
        while (factor <= (int(math.sqrt(number))) and number % factor != 0):
            factor += 2
    if (number % factor == 0):
        print("composite")
    else:
        print("prime")

while True:
    modFactorize()
    print("")

