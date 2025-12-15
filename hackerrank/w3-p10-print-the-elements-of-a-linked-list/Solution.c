#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct SinglyLinkedListNode
{
    int data;
    struct SinglyLinkedListNode *next;
} SinglyLinkedListNode;

typedef struct SinglyLinkedList
{
    SinglyLinkedListNode *head;
    SinglyLinkedListNode *tail;
} SinglyLinkedList;

SinglyLinkedListNode *create_singly_linked_list_node(int node_data)
{
    SinglyLinkedListNode *node = malloc(sizeof(*node));
    if (!node)
        exit(EXIT_FAILURE);
    node->data = node_data;
    node->next = NULL;
    return node;
}

void insert_node_into_singly_linked_list(SinglyLinkedList *list, int node_data)
{
    SinglyLinkedListNode *node = create_singly_linked_list_node(node_data);
    if (list->head == NULL)
    {
        list->head = node;
    }
    else
    {
        list->tail->next = node;
    }
    list->tail = node;
}

void printLinkedList(const SinglyLinkedListNode *head)
{
    while (head)
    {
        printf("%d\n", head->data);
        head = head->next;
    }
}

char *readline(void)
{
    size_t alloc_length = 1024, data_length = 0;
    char *data = malloc(alloc_length);
    if (!data)
        exit(EXIT_FAILURE);

    while (true)
    {
        char *cursor = data + data_length;
        if (!fgets(cursor, alloc_length - data_length, stdin))
            break;

        data_length += strlen(cursor);
        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n')
            break;

        alloc_length <<= 1;
        data = realloc(data, alloc_length);
        if (!data)
            exit(EXIT_FAILURE);
    }

    if (data[data_length - 1] == '\n')
        data[data_length - 1] = '\0';

    return realloc(data, data_length + 1);
}

int main(void)
{
    SinglyLinkedList list = {0};

    char *count_str = readline();
    int count = (int)strtol(count_str, NULL, 10);
    free(count_str);

    for (int i = 0; i < count; i++)
    {
        char *item_str = readline();
        int item = (int)strtol(item_str, NULL, 10);
        free(item_str);

        insert_node_into_singly_linked_list(&list, item);
    }

    printLinkedList(list.head);
    return EXIT_SUCCESS;
}
