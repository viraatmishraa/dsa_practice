import math
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)
def rotate(array,k):
    arrCpy=array
    array=array[k:]
    array=array+arrCpy[0:k]
    print(array)

def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    rotatingCoefficient=(inputNumber("by how much to rotate?:")%len(arr))
    rotate(arr,rotatingCoefficient)
main()