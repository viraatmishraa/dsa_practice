#include <stdio.h>
// int add(int ,int);

int main()
{
    int addPtr=add(10,20); 
    printf("%d",addPtr);
}

int add(int a, int b)
{
    return a;
}


int isUpper(char c)
{
    if (c>=65 && c<=91)
    return 1;
    else return 0;
}



// int (*addPtr)(int,int);
// //addPtr=add; 



/*Issues in the Code:
Global assignment issue:
addPtr = add; is declared at the global scope, but in C, global variables can only be initialized with constant expressions, not function addresses.
Function pointer assignments must be done inside a function, such as main().*/