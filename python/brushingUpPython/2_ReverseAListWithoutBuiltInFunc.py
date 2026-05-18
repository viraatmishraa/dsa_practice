def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

def reverse(arr):
    reversed=[]
    for i in range(len(arr)-1,-1,-1):
        reversed.append(arr[i])
    print(reversed)

def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    print (arr)
    reverse(arr)
main()