import math
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)
def search(searchedNumber,array):
    found=0
    for i in range(0,len(array)):
        if(searchedNumber==array[i]):
            print(f"target value is at index {i}")
            found=1
    if(found==0):
        print("target not found")





def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    target=inputNumber("enter target value:")
    search(target,arr)
main()