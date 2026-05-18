def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

def factorial(number):
    fact=1
    if(number<=0):       
        return 1
        #return fact     -> this was wrong
    # fact=number*factorial(number-1)   #  this is my code which is not working due to lack of proper return statements
    return number*factorial(number-1)

 
    




def main():
    number=inputNumber("enter the number:")
    print(factorial(number))
main()
