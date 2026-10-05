number = int(input ("Input the number for factorial :"))

def factorial(number) :
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial (number))