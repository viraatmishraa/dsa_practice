def main():
    string=input("enter string to be checked:")
    stringcp=string[::-1]
    if(string==stringcp):
        print("palindrome")
    else:
        print("not palindrome")
main()


