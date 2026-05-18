def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

stack=[]    

def pop():
    if(len(stack)==0):
        print("nothing to pop")
        return 
    stack.pop(len(stack)-1)

def insert(number):
    stack.append(number)
    return

def main():
    print("press 1 to insert \n press 2 to pop \n press 3 to print \n press 4 to quit")
    control=inputNumber("")
    while(control!=4):

        if(control==1):
            insert(inputNumber(""))
            print("Inserted! next?")
        if(control==2):
            pop()
        if(control==3):
            print(stack)
        if(control==4):
            print("invalid input")

        control=inputNumber("")
main()