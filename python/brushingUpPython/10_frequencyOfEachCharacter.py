
def frequency(string):
    map={}
    for i in string:
        if i in map:
            map[i]+=1
        else: 
            map[i]=1
    for i in map:
        print(f"{i} is {map[i]} times in the string")


def main():
    string=input("enter string to be checked")
    frequency(string)
    print (string)
main()