// //rewrite delete function to which uses two pointers

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

struct node * deleteAtIndex(struct node* head, int x)
{
    struct node * headCopy=head;
    //exception handling
    
    int counter=0;
    if(head==NULL)
    {
        printf("list is empty\n");
        return head;
    }
    struct node * temp;
        if(x==0)
        {
            head=head->next;
            return head;//'''''''''''''''''''''''
        }             
    while(head!=NULL)
    {
        if (counter==(x-1))
        {   
            temp=head;
            break;
        }
        head=head->next;
        counter ++;
    }
    temp->next=temp->next->next;
    return headCopy;

}





int main()
{
    struct node * head = NULL;
    head=create(head,1);
    head=create(head,2);
    head=create(head,3);
    head=create(head,4);
    head=create(head,5);
    head=deleteAtIndex(head,2);
    if (head==NULL)
    exit(0);   
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



// the commented part is supposed to be the body, 
// however for the sake of the accuracy of the name
// of this program, all of the body is commented
