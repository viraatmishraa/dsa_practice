/*This means:  

1. **Write a program** that attempts to use a pointer without initializing it.  
2. **Observe the segmentation fault** that occurs when trying to dereference an uninitialized pointer.  
3. **Fix the issue** by properly initializing the pointer before use.*/
#include <stdio.h>
int main()
{
   // int * p=NULL;---------- causes segmentation err
   int *p; //does not cause segmentation error due to compiler, this statement will lead to inpredictable behaviour, thats it
    printf("%d,%d",*p+1,p);
}


