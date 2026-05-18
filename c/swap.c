#include <stdio.h>
int swap(int * a,  int*  b);
int main()
{
    int x=10,y=20;
    printf("%d=a %d=b is swapping ke pehle",x,y);

    swap(&x,&y);
    printf("%d=a %d=b is swapping ke bad",x,y);
}
int swap (int *a, int *b)
{
    int c= *a;//this was a little complex  because of lack of practice  
    *a=*b;
    *b=c;
    return 0;
}