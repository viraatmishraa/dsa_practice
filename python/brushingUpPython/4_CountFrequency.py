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
    for i in arr:
        if i in map:
            map[i]+=1
        else: 
            map[i]=1
    for i in map:
        print(f"{i} is {map[i]} times in the array\n")


def main():
    arr=[]
    for i in range(0,inputNumber("enter size of array")):
        arr.append(inputNumber("enter input:"))
    frequency(arr)
    print (arr)
main()