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

struct node * deleteAtElement(struct node* head, int searchedElement)
{
    //exception handling
    

    if(head==NULL)
    {
        printf("list is empty\n");
        return head;
    }
    struct node * temp=head;
    
    while(temp->next!=NULL)
    {
        if (temp->data==searchedElement)
        {   
            break;
        }
        temp=temp->next;
    }
    
    temp->next=temp->next->next;
    return head;

}





int main()
{
    struct node * head = NULL;
    head=create(head,12);
    head=create(head,23);
    head=create(head,34);
    head=create(head,45);
    head=create(head,56);
    head=deleteAtElement(head,12);//the program is deleting the next element to the target element
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
