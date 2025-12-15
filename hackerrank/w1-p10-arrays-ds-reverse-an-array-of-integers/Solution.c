#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

char *readline();
char *ltrim(char *);
char *rtrim(char *);
char **split_string(char *);
int parse_int(char *);

int *reverseArray(int a_count, int *a, int *result_count)
{
    *result_count = a_count;
    int *rev = malloc(a_count * sizeof(int));
    for (int i = 0; i < a_count; i++)
    {
        rev[i] = a[a_count - 1 - i];
    }
    return rev;
}

int main()
{
    FILE *fptr = fopen(getenv("OUTPUT_PATH"), "w");

    int arr_count = parse_int(ltrim(rtrim(readline())));
    char **arr_temp = split_string(rtrim(readline()));

    int *arr = malloc(arr_count * sizeof(int));
    for (int i = 0; i < arr_count; i++)
    {
        arr[i] = parse_int(arr_temp[i]);
    }

    int res_count;
    int *res = reverseArray(arr_count, arr, &res_count);

    for (int i = 0; i < res_count; i++)
    {
        fprintf(fptr, "%d", res[i]);
        if (i < res_count - 1)
        {
            fprintf(fptr, " ");
        }
    }
    fprintf(fptr, "\n");

    free(arr);
    free(res);

    fclose(fptr);
    return 0;
}

char *readline()
{
    size_t alloc_length = 1024, data_length = 0;
    char *data = malloc(alloc_length);

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
    }

    if (data[data_length - 1] == '\n')
    {
        data[--data_length] = '\0';
    }
    data = realloc(data, data_length + 1);
    return data;
}

char *ltrim(char *str)
{
    while (*str && isspace(*str))
        str++;
    return str;
}

char *rtrim(char *str)
{
    char *end = str + strlen(str) - 1;
    while (end >= str && isspace(*end))
        end--;
    end[1] = '\0';
    return str;
}

char **split_string(char *str)
{
    char **splits = NULL;
    char *token = strtok(str, " ");
    int count = 0;

    while (token)
    {
        splits = realloc(splits, sizeof(char *) * ++count);
        splits[count - 1] = token;
        token = strtok(NULL, " ");
    }
    return splits;
}

int parse_int(char *str)
{
    char *endptr;
    int value = strtol(str, &endptr, 10);
    if (endptr == str || *endptr != '\0')
        exit(EXIT_FAILURE);
    return value;
}
