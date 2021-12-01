#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_int(int number)
{
}

void insert_sort(int *arr, int length)
{
    int i,j;
    for (i=0; i < length; i++) {
        j = i+1;
        while (j > 0) {
            if (arr[j-1] > arr[j]) {
                int temp = arr[j-1];
                arr[j-1]=arr[j];
                arr[j] = temp;
            }
            j--;
        }
    }
}

int main(int argc, char *argv[])
{
    const int arr_sample[] = {4,7,2,23,54,1,23,12,89,7,9,16,11,12,6};
    int *arr = malloc(sizeof(arr_sample));
    memcpy(arr, arr_sample, sizeof(arr_sample));
    int length = sizeof(arr_sample)/sizeof(*arr_sample);

    int i;
    for (i=0; i<length; i++)
        printf("%d ", arr[i]);
    printf("\n");

    insert_sort(arr, length);

    for (i=0; i<length; i++)
        printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
