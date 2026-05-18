import math
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)


def sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                copy=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=copy
    return arr

def BinarySearch(searchedNumber,array):
    sortedArray=sort(array)
    found=None
    start=0
    end=len(sortedArray)-1
    while(start<=end):
        mid=(start+end)//2
        if(searchedNumber==sortedArray[mid]):
            return mid
        elif(searchedNumber>sortedArray[mid]):
            start=mid+1
        elif(searchedNumber<sortedArray[mid]):
            end=mid-1
    return-1


def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    target=inputNumber("enter target:")
    sort(arr)
    index=BinarySearch(target,arr)
    if(index==-1):
        print("no match")
    else:
        print(f"target:{target} found at index:{index}")
    # search(target,arr)
main()