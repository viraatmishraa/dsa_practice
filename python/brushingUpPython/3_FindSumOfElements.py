
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)
    
def sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    print(f"the sum is {sum}")

def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    print(arr)
    sum(arr)
main()
