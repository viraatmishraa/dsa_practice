#include <stdio.h>
#include <stdlib.h>
int main()
{
    int * x=(int *)malloc(sizeof(int));

   // for (int i=0;i<=10;i++) this was creating problem as realloc was fed 0 as an input
   for (int i=1;i<=10;i++)  
   {
        x= realloc(x,(sizeof(int)*i));

    }
    for(int i=0;i<=9/*this was going out of bound*/;i++)
    {
        x[i]=i;
    }
    for(int i=0;i<=10;i++)
    {
        printf("%d,",x[i]);
    }
}