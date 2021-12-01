#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void swap(int *arr, int i, int j)
{
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j]  = temp;
}

/* in-place sort, can be done in O(n*log(n)) time */
void sort_array(int *arr, int length)
{
  int i;
  int j;
  for (i=0; i < length; i++)
    for (j=i+1; j < length; j++)
      if (arr[i] > arr[j])
        swap(arr, i, j);
      
}

int main(int argc, char *argv[])
{
  int size = 100;
  int print_result = 1;
  
  if (argc > 1)
  {
    size = atoi(argv[1]);
    print_result = 0;
  }
  int *arr = malloc(size * sizeof(int));
  
  srand(time(NULL));
  
  printf("Allocate data...\n");
  
  for (int i=0; i < size; i++)
  {
    arr[i] = rand();
  }
  
  printf("Sort data...\n");
  
  sort_array(arr, size);
  
  if (print_result)
  {
    for (int i=0; i < size; i++)
    {
      printf("%d\n", arr[i]);
    }
  }

  return 0;
}
