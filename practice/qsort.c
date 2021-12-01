
/* algorithm to check if a string has all unique characters */

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

// - add all characters to a dictionary.
// - can sort? sort and check.

void swap(int *arr, int i, int j)
{
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

int partition(int *arr, int length, int pivot)
{
#if 1
  int i = 0;
	int j = length - 1;
	
	while (1)
	{
		while (arr[i] < pivot)
      i++;
		while (arr[j] > pivot)
      j--;
    
    if (i >= j)
      break;
    
		swap(arr, i, j);
    i++;
    j--;
	}
#else
	int i = -1;
	int j = length;
	
	while (i < j)
	{
    do
      i++;
	  while (arr[i] < pivot);
    do
      j--;
		while (arr[j] > pivot);

    if (i >= j)
      break;
    
		swap(arr, i, j);
	}
#endif
	return j;
}

typedef struct sort_qe
{
	struct sort_qe *next;
	int *arr;
	int length;
} sort_qe;

sort_qe *sort_q;

unsigned alloc_size;
unsigned max_alloc;

void sort_array(int *arr, int length)
{
	sort_qe *qe = malloc(sizeof(sort_qe));
	qe->arr = arr;
	qe->length = length;
	qe->next = NULL;
	sort_q = qe;
	
	while (sort_q)
	{
		qe = sort_q;
		sort_q = sort_q->next;
		
    int pos = partition(qe->arr, qe->length, qe->arr[qe->length/2-1]);
    
    if (pos > 0)
    {
      sort_qe *left_qe = malloc(sizeof(sort_qe));
      alloc_size += sizeof(sort_qe);
      left_qe->arr = qe->arr;
      left_qe->length = pos + 1;
      left_qe->next = sort_q;
      sort_q = left_qe;
    }
    if (pos < qe->length - 2)
    {
      sort_qe *right_qe = malloc(sizeof(sort_qe));
      alloc_size += sizeof(sort_qe);
      right_qe->arr = &qe->arr[pos+1];
      right_qe->length = qe->length - pos - 1;
      right_qe->next = sort_q;
      sort_q = right_qe;
    }
    if (alloc_size > max_alloc)
      max_alloc = alloc_size;
  
	  free(qe);
    alloc_size -= sizeof(sort_qe);
  }
}

int main(int argc, char *argv[])
{
	int length = 1000;
	int print_result = 1;
	int i;
	
	if (argc > 1)
	{
		length = atoi(argv[1]);
		print_result = 0;
	}
	
	printf("size: %u\n", length);
	
	int *arr = malloc(sizeof(*arr) * length);
	
	srand(time(NULL));
  
  printf("allocating...\n");
	
	for (i=0; i < length; i++)
	{
		arr[i] = rand();
	}
	
  printf("sorting...\n");
  
	sort_array(arr, length);
  
  printf("checking...\n");
  
  int prev = 0;
  for (i=0; i<length; i++)
  {
    if (prev > arr[i])
      printf("sorting error: [%u]: %u > %u\n", i, prev, arr[i]);
    prev = arr[i];
  }
  
  printf("done, max_alloc: %u\n", max_alloc);
	
	return 0;
}
