def main():
    string1=input("enter string 1:")
    string2=input("enter string 2:")
    map1={}
    map2={}
    for i in string1:
        if i in map1:
           map1[i]+=1
        else: 
           map1[i]=1
    for i in string2:
        if i in map2:
           map2[i]+=1
        else: 
           map2[i]=1
    if map1==map2:
       print("anagram")
    else:
       print("not anagram")
           
main()