import math
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)



def MinMax(array):
    max=(-math.inf)
    min=math.inf
    for i in array:
        if(min>i):
            min=i
        if(max<i):
            max=i
    print(f"Max is={max} Min is={min}")

def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    print (arr)
    MinMax(arr)
main()