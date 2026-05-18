def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

def fibonacci(number,answer1,answer2):
    cpy=answer2
    answer2=answer2+answer1
    answer1=cpy
    if(number==0):
        return 1
    return (answer1+fibonacci(number-1,answer1,answer2))
 
def main():
    number=inputNumber("enter the number:")
    if(number==0):
        print(0)
    if(number==1):
        print(1)
    if(number==2):
        print(fibonacci(number-2,0,1))
main()
