struct Node {
    int data;
    struct Node *prev, *next;
};
struct Node* sortedInsert(struct Node* head, int x) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->prev = newNode->next = NULL;
    
    // 1. empty list
    if(head == NULL) {
        return newNode;
    }
    
    // 2. insert before head
    if(x <= head->data) {
        newNode->next = head;
        head->prev = newNode;
        return newNode;
    }
    
    // 3. insert inn middle or end
    struct Node* curr = head;
    while (curr->next && curr->next->data < x) {
        curr = curr->next;
    }
    newNode->next = curr->next;
    if (curr->next) {
        curr->next->prev = newNode;
    }
    curr->next = newNode;
    newNode->prev = curr;
    
    return head;
}
