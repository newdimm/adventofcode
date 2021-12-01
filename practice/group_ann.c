#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char **arr, int a, int b)
{
  char *tmp = arr[a];
  arr[a] = arr[b];
  arr[b] = tmp;
}

void load_counters(int *counters, char *s)
{
  while (*s)
  {
    counters[*s]++;
    s++;
  }
}

int check_counters(int *counters, char *s)
{
  while (*s)
  {
    if (!counters[*s])
      return 0;
    counters[*s]--;
    s++;
  }
  int i=0;
  for (i=0; i<256; i++)
  {
    if (counters[i])
      return 0;
  }
  return 1;
}

void group_ann(char **arr, int len)
{
  /* Sort array of strings so that all annagrams are next to each other */
  int i = 0;
  
  while (i < len)
  {
    int c_i[256];
    memset(c_i, 0, sizeof(c_i));
    load_counters(c_i, arr[i]);
    
    int j;
    for (j=i+1; j < len; j++)
    {
      int c_j[256];
      memset(c_j, 0, sizeof(c_j));
      load_counters(c_j, arr[j]);
      if (memcmp(c_i, c_j, sizeof(c_j)) == 0)
      {
        if (j != i + 1)
        {
          swap(arr, i+1, j);
        }
        i++;
      }
    }
    i++;
  }
}


int main(int argc, char *argv[])
{
  char *a = "listen";
  char *b = "silent";
  char *c = "lentis";
  char *d = "lentus";
  char *e = "sulent";
  char *f = "ublent";
  char *g = "ulbent";
  char *h = "baslet";
  int len = 8;
  char **arr = malloc(sizeof(char *)*len);
  arr[0] = h;
  arr[1] = a;
  arr[2] = c;
  arr[3] = d;
  arr[4] = g;
  arr[5] = b;
  arr[6] = e;
  arr[7] = f;
  
  int i;
  for (i=0; i<len; i++)
    printf("[%d]: <%s>\n", i, arr[i]);
  
  group_ann(arr, len);
  
  printf("\n");
  
  for (i=0; i<len; i++)
    printf("[%d]: <%s>\n", i, arr[i]);
  
  return 0;
}
