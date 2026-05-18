def main():
    string=input("enter string to be checked:")
    consonants={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','M','N','B','V','C','X','Z','L','K','J','H','G','F','D','S','P','Y','T','R','W','Q'}
    vowels={'A','E','I','O','U','a','e','i','u','o'}
    noOfConsonants=0
    noOfVowels=0
    for i in string:
        if i in vowels:
            noOfVowels=noOfVowels+1
        if i in consonants:
            noOfConsonants=noOfConsonants+1
    print(f"no of vowels={noOfVowels} and no of consonants={noOfConsonants}")
main()