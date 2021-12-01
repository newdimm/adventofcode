#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sorted_merge(int *a, int len_a, int *b, int len_b)
{
  /* A and B are sorted arrays, A has enough space at the end to hold B.
  Merge them in a sorted order. */
  int pos_c = len_a + len_b - 1;
  int pos_a = len_a - 1;
  int pos_b = len_b - 1;
  while (pos_c >= 0 && pos_b >= 0)
  {
    if (a[pos_a] > b[pos_b])
    {
      a[pos_c] = a[pos_a];
      pos_a--;
    }
    else {
      a[pos_c] = b[pos_b];
      pos_b--;
    }
    pos_c--;
  }
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

void print_int(int *a, int len)
{
  int i;
  for (i=0; i < len; i++)
  {
    printf("%d ", a[i]);
  }
  printf("\n");
}

int main(int argc, char *argv[])
{
  int len_a;
  int len_b;
  const int a_sample[] = {3,5,6,2,5,9,56,4,3,2,23,12,11};
  const int b_sample[] = {4,10,12,14,15,3,6,32,6,17};
  int *a = malloc(sizeof(a_sample)+sizeof(b_sample));
  int *b = malloc(sizeof(b_sample));
  memset(a, 0, sizeof(a_sample)+sizeof(b_sample));
  memcpy(a, a_sample, sizeof(a_sample));
  memcpy(b, b_sample, sizeof(b_sample));
  
  len_a = sizeof(a_sample) / sizeof(*a_sample);
  len_b = sizeof(b_sample) / sizeof(*b_sample);
  
  print_int(a, len_a);
  print_int(b, len_b);
  
  insert_sort(a, len_a);
  insert_sort(b, len_b);

  print_int(a, len_a);
  print_int(b, len_b);

  sorted_merge(a, len_a, b, len_b);

  print_int(a, len_a + len_b);
  
  return 0;
}
