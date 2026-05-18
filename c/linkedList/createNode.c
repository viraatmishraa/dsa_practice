/* this program have a create, print and traverse funciton */


#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node * next;
};


int printlist(struct node * head);
struct node * create(struct node * head,int x);
struct node * traverse(struct node * head);


int main()
{
    struct node * head = NULL;
    head=create(head,1);
    head=create(head,2);
    head=create(head,3);
    head=create(head,4);
    head=create(head,5);

    
    
    printlist(head);
    return 0;
}


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
        struct node * temp=traverse(head);
        newnode->data=x;
        temp->next=newnode;
        newnode->next=NULL;
    }
    return head;
}


struct node * traverse(struct node * head)
{
    while (head->next!=NULL)
    {
        head = head->next;
    }
    return head;
}

int printlist(struct node * head)
{
    while(head->next!=NULL)
    {
        printf("%d --->",head->data);
        head=head->next;
    }
        printf("%d",(head->data));
}
