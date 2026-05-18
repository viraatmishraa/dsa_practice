#include <stdio.h>
int main()
{
    int rows=4,columns=4;
 int a[4][4]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};

//  printf("%-12d,   a\t\n",a);
//  printf("%-12d,  *a\t\n",*a);
//  printf("%-12d,  **a\t\n",**a);
//  printf("%-12d,  a+1\t\n",a+1);
//  printf("%-12d,  *(a+1)\n",*(a+1));
//  printf("%-12d,  **(a+1)\t\n",**(a+1));
//  printf("%-12d,  a+2\t\n",a+2)  ;
//  printf("%-12d,  *a+2\t\n",*a+2);
//  printf("%-12d,  **a+2\t\n",**a+2);
//  printf("%-12d,  a+1\t\n",a+1+2);
//  printf("%-12d,  *(a+1)\n",*(a+1)+2);
//  printf("%-12d,  **(a+1)\t\n",**(a+1)+2);
//  printf("%-12d,  *(*a+1)+2)\t\n",*(*a+1)+2);
//  printf("%-12d,  a+1\t\n",*a+1+2);
//  printf("%-12d,  *(*a+1)+2\n",*(*a+1)+2);

 //printf("%-12d,  **(a+1)\t\n",**(a+1)+2);

 //printf("%-12d,  *(*(a+1)+2)\t\n",*(*(*a+1)+2));



 for (int i = 0; i < rows; i++)
 {
    for(int j = 0;j < columns;j++)
    {
        if( (i==0 || j==0) || (i==rows-1 || j==columns-1))
        {
            printf(" %d,",*(*(a+i)+j)) ;
            //wrogn expression -*(*a+i)+j)
        }else
        printf("   ,");
    }
        printf("\n");
 }
// very interesting ->printf("%d %d %d",**a,**a+1,**(a+14);

}
    



 
 
 
 
 



