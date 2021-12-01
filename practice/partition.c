#include <stdio.h>
#include <stdlib.h>

typedef struct le
{
    int value;
    struct le *next;
} le;

le *list;


void print_list(le *list)
{
    while (list)
    {
        printf("%d ", list->value);
        list = list->next;
    }
    printf("\n");
}

le *partition(le *list, int pivot)
{
    le *left_ptr = NULL;
    le *right_ptr = NULL;
    le *forward = list;
    le **left_next;
    int left = (list->value < pivot) ? 1 : 0;

    while (forward)
    {
        if (!forward->next ||
                forward->next->value < pivot && !left ||
                forward->next->value >= pivot && left)
        {
            le *next = forward->next;
            if (left)
            {
                if (!left_ptr)
                {
                    left_next = &forward->next;
                }
                forward->next = left_ptr;
                left_ptr = list;
            }
            else
            {   
                forward->next = right_ptr;
                right_ptr = list;
            }
            forward = next;
            list = forward;
            left = !left;
        }
        else
        {
            forward = forward->next;
        }
    }

    if (left_ptr)
    {
        *left_next = right_ptr;
    }
    else
    {
        left_ptr = right_ptr;
    }
    return left_ptr;
}

int main(int argc, char *argv[])
{
    const int arr[] = {3, 5, 6, 23, 5, 7, 2, 3, 7, 9, 2, 1 ,2 ,4 ,5, 7, 6, 8, 10, 2, 3, 3 ,4 ,2 ,3 ,4, 10};
    
    int i;
    int count = sizeof(arr)/sizeof(*arr);
    for (i=0; i<count; i++)
    {
        le *entry = malloc(sizeof(le));
        entry->value = arr[i];
        entry->next = list;
        list = entry;
    }


    print_list(list);


    list = partition(list, 5);

    print_list(list);

    return 0;
}
