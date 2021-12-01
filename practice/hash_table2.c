/* find if two strings are permutations or each other */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct ht_entry
{
  struct ht_entry *next;
  int value;
} ht_entry;

ht_entry **ht;
int ht_size;

int mapping_function(int value, int ht_size)
{
	return value % ht_size;
}

ht_entry **hash_alloc(int ht_size)
{
  ht_entry **ht = malloc(sizeof(*ht) * ht_size);
  if (ht)
    memset(ht, 0, sizeof(*ht) * ht_size);
  return ht;
}

void hash_free(ht_entry **ht, int ht_size)
{
  int i;

  for (i=0; i<ht_size; i++)
  {
    ht_entry *hte = ht[i];
    
    while (hte)
    {
      ht_entry *tmp = hte;
      hte = hte->next;
      free(tmp);
    }
  }
  
  free(ht);
}

int check_perm(int *a, int *b, int length)
{
  int i;
  int result = 1;
  ht_size = length;
  
  printf("allocatiing hash table size %u...\n", ht_size);
  
  ht = hash_alloc(ht_size);
  if (!ht)
    return -1;

  printf("filling hash table...\n");
  
  for (i=0; i<length; i++)
  {
    int value = a[i];
	  int index = mapping_function(value, ht_size);
    //printf("[%u] %u -> %u\n", i, value, index);
    
    ht_entry *hte = malloc(sizeof(ht_entry));
    if (!hte)
      return -1;
    hte->value = value;
    hte->next = ht[index];
    ht[index] = hte;
  }

  printf("checking hash table...\n");
  
  for (i=0; i<length; i++)
  {
    int value = b[i];
    int index = mapping_function(value, ht_size);
    int found = 0;
    //printf("?[%u] %u -> %u\n", i, value, index);

    ht_entry **pp = &ht[index];
    while (*pp)
    {
      if ((*pp)->value == value)
      {
        ht_entry *hte = *pp;
        *pp = hte->next;
        free(hte);
        found = 1;
        break;
      }
      pp = &(*pp)->next;
    }
    if (!found)
    {
      result = 0;
      break;
    }
  }
  
  printf("freeing hash table...\n");
  
  if (result == 0)
  {
    hash_free(ht, ht_size);
  }
  else
    free(ht);
  return result;
}


int main(int argc, char *argv[])
{
  int size = 10;
  if (argc > 1)
    size = atoi(argv[1]);
  
  printf("size: %u\n", size);
  
  printf("generating...\n");
  int i;
  int *a, *b, *c;
  a = malloc(sizeof(*a)*size);
  b = malloc(sizeof(*b)*size);
  c = malloc(sizeof(*c)*size);
  if (!a || !b || !c)
    return -1;
  srand(time(NULL));
  for (i=0; i < size; i++)
  {
    a[i] = rand();
    b[size - i - 1] = a[i];
    c[i] = a[i] + 1;
  }
  printf("checking 1...\n");
  int result = check_perm(a,b,size);
  printf("result: %d %s\n", result, (result == 1) ? "PASS":"FAIL");

  printf("checking 2...\n");
  result = check_perm(a,c,size);
  printf("result: %d %s\n", result, (result == 0) ? "PASS":"FAIL");
    
  return 0;
}