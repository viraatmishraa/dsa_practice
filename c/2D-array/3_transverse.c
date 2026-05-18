#include <stdio.h>
swap(int * a,int * b)
{
    int c=*a;
     *a=*b;
     *b=c;

}
int main()
{
    int array[4][4]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
    for (int i =0 ;i<=3;i++)
    {
    for (int j =0 ;j<=3;j++)
    {
        if(array[i][j]<10)
        printf(" %d,",array[i][j]);
        else
        printf("%d,",array[i][j]);

    }
    printf("\n");
    }
for(int i=0;i<4;i++)
{
    for (int j =0 ;j<=i;j++)
        {
            if(i!=j)
            swap(&array[i][j],&array[j][i]);
        }
}
//printing beautifully wala funtion
for (int i =0 ;i<=3;i++)
{
for (int j =0 ;j<=3;j++)
{
    if(array[i][j]<10)
    printf(" %d,",array[i][j]);
    else
    printf("%d,",array[i][j]);

}
printf("\n");
}

}
