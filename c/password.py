#choice for the user if he wants to continue with the same password or not
def choice():
    print("do you want to re-enter your password? y/n\n")
    c=input()
    if c=='y' or c=='Y':
        password()
    elif c=='n' or c=='N':
        return 0
    else:
        print("invalid choice, press 'y' for yes and 'n' for no")
        choice()  

#-------------------------------------------------------------------    
    
def password():

    p=input("enter your password:\n")

    c=0
    #to check if then password has any spaces
    for i in p:
        if i==" ":
            c=c+1
    if c>=1:
        print("kindly dont use space in your password:\n")
        password()

    #if the length of the password is less than 4 its very weak
    if len(p)<=4: 
        print("very weak password:\npassword is too small:\n")
        choice()
    # if len(p)>=10:
    #     print("password is too long\nmake it smaller:\n")
    #     password()

    # #if all elements are capital letters or small letters or digits then the pass is weak
    else:         
        c1=0
        c2=0
        c3=0
        for i in p:
            if i.isupper():
                c1=c1+1
            elif i.islower():
                c2=c2+1
            elif i.isdigit():
                c3=c3+1
        if c1==len(p) or c2==len(p) or c3==len(p):
            print("weak password:\n")
            choice()

        #if the pass contains a mixture of any two -capital letters, small let, numbers
        #then the strength of the password is medium

        c1=0
        c2=0
        c3=0

        for i in p:
            if i.isupper():
                c1=c1+1
            if i.islower():
                c2=c2+1
            if i.isdigit():
                c3=c3+1

        if c1>0 and c1<len(p) and c2>0 and c2<len(p) and c3==0:
            print("medium level password:\n")
            choice()

        elif c3>0 and c3<len(p) and c2>0 and c2<len(p) and c1==0:
            print("medium level password:\n")
            choice()

        elif c3>0 and c3<len(p) and c1>0 and c1<len(p) and c2==0:
            print("medium level password:\n")
            choice()
        
        elif c3>0 and c3<len(p) and c1>0 and c1<len(p) and c2>0 and c2<len(p):
            print("strong password:\n")
            choice()
        
        else:
            print("very strong password")
            return 0
password()