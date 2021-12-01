/* find if two strings are permutations or each other */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

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

int check_perm(int *a, int *b, int length)
{
  int i;
  
  sort_array(a, length);
  sort_array(b, length);
  
  for (i=0; i<length; i++)
  {
    if (a[i] != b[i])
      return 0;
  }
  return 1;
}


int main(int argc, char *argv[])
{
  int size = 10;
  if (argc > 1)
    size = atoi(argv[1]);
  
  printf("size: %u\n", size);
  
  printf("generating...\n");
  int i;
  int *a,* a1, *b, *c;
  a = malloc(sizeof(*a)*size);
  a1 = malloc(sizeof(*a)*size);
  b = malloc(sizeof(*b)*size);
  c = malloc(sizeof(*c)*size);
  if (!a || !b || !c)
    return -1;
  srand(time(NULL));
  for (i=0; i < size; i++)
  {
    a[i] = rand();
    a1[i] = a[i];
    b[size - i - 1] = a[i];
    c[i] = a[i] + 1;
  }
  printf("checking 1...\n");
  int result = check_perm(a,b,size);
  printf("result: %d %s\n", result, (result == 1) ? "PASS":"FAIL");

  printf("checking 2...\n");
  result = check_perm(a1,c,size);
  printf("result: %d %s\n", result, (result == 0) ? "PASS":"FAIL");
    
  return 0;
}