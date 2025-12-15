/*
struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
};
*/
struct Node* reverse(struct Node* head) {
    struct Node* temp = NULL;
    struct Node* curr = head;

    while (curr != NULL) {
        // swap next and prev
        temp = curr->prev;
        curr->prev = curr->next;
        curr->next = temp;
        // move to next node (curr->prev)
        curr = curr->prev;
    }

    // adjust head to the new front node
    if (temp != NULL)
        head = temp->prev;

    return head;
}
