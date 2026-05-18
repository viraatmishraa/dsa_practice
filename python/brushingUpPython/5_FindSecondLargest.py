import math
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)



def Max(array):
    max=(-math.inf)
    for i in array:
        if(max<i):
            max=i
    return max

def secondLargest(array,max):
    secondmax=-math.inf
    for i in array:
        if (i<max and i>secondmax):
            secondmax=i
    if(secondmax<-math.inf):    
        print(f"second largest is {secondmax}")
    else:
        print("no second largest available")

def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    print (arr)
    max=Max(arr)
    secondLargest(arr,max)
main()