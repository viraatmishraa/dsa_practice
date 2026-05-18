def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

def palindrome(number,spine):
    spine=spine*10+(number%10)
    if(number<=0):       
        return 0
    return (palindrome(number//10,spine)*10)+spine


def main():
    number=inputNumber("enter the number:")
    print(palindrome(number,0))
main()