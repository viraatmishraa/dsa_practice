def inputNumber(str):
    x=input(str)
    try:
        x=int(x)
        return x
    except:
        print("invalid input")
        return inputNumber(str)

def frequency(arr):
    map={}
    arrcp=arr[:]
    #arrcp=arr does not create a copy of the object
    # instead both point to the same object hence
    # iterating to the same.
    for i in arrcp:
        if i in map:
            arr.remove(i)
        else: 
            map[i]=1
    print(arr)

def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    frequency(arr)
main()