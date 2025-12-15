int getKthFromLast(struct Node* head, int k) {
    struct Node* curr = head;
    int count = 0;
    while(curr) {
        curr = curr->next;
        count++;
    }
    if(k>count) {
        return -1;
    } else {
        for(int i=0; i<(count-k); i++) {
            head = head->next;
        }
        return head->data;
    }
}
