import math
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)



def Min(array):
   
    min=math.inf
    index=0
    for i in array:
        if(min>i):
            min=i
            minIndex=index
        index=index+1
    return [min,minIndex]
    # print(f"Max is={max} Min is={min}")
def selectionSort(array):
    for i in range(0,len(array)):
        smallest=Min(array[i:])
        array[smallest[1]+i]=array[i]

        array[i]=smallest[0]
    print(array)


def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
    # print (arr)
        arr.append(inputNumber("enter input:"))
    selectionSort(arr)
main()