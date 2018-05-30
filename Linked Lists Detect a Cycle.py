/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    if (head == NULL){return false;}
    if (head->next == NULL){return false;}
    Node *t,*tt;
    tt = head;
    t = tt;
    while(tt->next != NULL){
        tt=tt->next;
        if (tt == t){ return true;}
        if (tt->next == NULL){return false;}
        tt=tt->next;
        if (tt == t){ return true;}
        t=t->next;
    }
    return false;
}
