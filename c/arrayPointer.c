/*Declare an array and use a pointer to access and modify its elements using pointer arithmetic instead of array indexing.
Print memory addresses of the array elements and compare them to understand how they are stored in memory.
*/

#include<stdio.h>
int main()
{
    double arr[5]={1,2,3,4,5};
    for (int i=0;i<5;i++)
    {
        printf("\n%d\n",(arr)+i);
    }
}
