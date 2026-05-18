/*print the snake pattern, take n as input for n*m
   |<-  1    ->  2    ->  3    ->  4  ->|
   V->  8    <-  7    <-  6    <-  5  <-V
   |<-  9    -> 10    -> 11    -> 12  ->|
   V->  16   <- 15    <- 14    <- 13  <-V
*/
#include <stdio.h>
#include <stdlib.h>
int input(int * num)
{
    printf("enter a valid interger\n");
    if(scanf("%d",num)==1)
    {   
        return *num;
    }
    else
    {   
         printf("\n\ninvalid input\n\n");
         exit(0);
    }
}

// use the format--   int ram = input(&ram);

int main()
{
    int i,j;//loop sentinels
    int x=1,pre_x=0,pre_j=0;
    int n = input(&n);
    for(i=1;i<=n;i++)
    {
        if((i%2))
        {
            for ( j = x; j <= x+n ; j++)//odd lines
            {
                printf("%d ",j+pre_j); 
            }
            pre_j=x+n;
            printf("\n");
        }
        if(!(i%2))
        {
            for ( j = pre_j; j>=pre_j-n ; j--)//even lines
            {
                printf("%d ",j+pre_j);               
            }
            x=pre_j+1;
            printf("\n");    
        }
    }
}