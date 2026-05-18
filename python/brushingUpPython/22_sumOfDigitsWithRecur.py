def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

def sumOfDigit(number):
    sum=0
    if(number<=0):       
        return 0
    return number%10+sumOfDigit(number//10)

 
    




def main():
    number=inputNumber("enter the number:")
    print(sumOfDigit(number))
main()
