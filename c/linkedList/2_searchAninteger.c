//assume thet we have a list of integers. create a fucntion that searches for an integer and returns the addrss of the node, else NULL
#include <stdio.h>
#include <stdlib.h>

struct node 
{
    int data;
    struct node * next;
} ;

struct node * create(struct node * head,int x)
{
    struct node * newnode= (struct node *)(malloc(sizeof(struct node)));
    if(head==NULL)
    {
        newnode->data=x;
        head= newnode;
        newnode->next=NULL;
    }
    else
    {
        struct node * temp=head;
        while (temp->next!=NULL)
        {
            temp = temp->next;
        }
        newnode->data=x;
        temp->next=newnode;
        newnode->next=NULL;
    }
    return head;
}

struct node * search(struct node * head,int searchedElement)
{
    while(head!=NULL)
    {   
    // printf("%d\n",head->data);
        if(head->data==searchedElement)
        {
            return head;
        }
        head=head->next;
    }
    
    
        printf("%d notfound\n",searchedElement);
        return NULL;
    
}
int printlist(struct node * head)
{
    while(head->next!=NULL)
    {
        printf("%d --->",head->data);
        head=head->next;
    }
        printf("%d",(head->data));
        return 0;
}
int main()
{
    struct node * head = NULL;
    head=create(head,1);
    head=create(head,2);
    head=create(head,3);
    head=create(head,4);
    head=create(head,5);
    
    // printlist(head);
    int x = 5 ;
    struct node * searchedElementAddress=search(head,x);
    if(searchedElementAddress!=NULL)
        printf("%d is present in the list",*searchedElementAddress);
  
    return 0;
}