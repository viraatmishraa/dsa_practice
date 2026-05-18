def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

stack=[]    

def pop(top): 
    stack.pop(len(stack)-1)
    top=top-1
    return top


def push(number,top):
    stack.append(number)
    top=top+1
    return top

def main():
   string=list(input("enter the arguement:"))
   print(string)
   top=0
   for i in string:
        if(i=='('or i=='{'or i=='('):
            top=push(i,top)
            print(stack)

        if(i==')'or i==']'or i=='}'):    
            if(ord(i)==ord(string[top])+2 or ord(i)==ord(string[top])+1):
                top=pop(top)
                print(stack)
        # else:
        #     print("invalid paranthesis")
main()
