#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void zero(int **a, int N, int M)
{
	int temp;
  int i,j;
  int *ii = malloc(sizeof(int) * N);
  int *jj = malloc(sizeof(int) * M);
  for (i=0; i<N; i++)
    ii[i] = 1;
  for (j=0; j<M; j++)
    jj[j] = 1;

  printf("1\n");
    
  for (i=0; i<N; i++)
  {
    for (j=0; j<M; j++)
    {
      if (a[i][j] == 0)
      {
        ii[i] = 0;
        jj[j] = 0;
      }
    }
  }
  
  printf("2\n");
  
  for (i=0; i<N; i++)
  {
    for (j=0; j<M; j++)
    {
      if (ii[i] == 0 || jj[j] == 0)
         a[i][j] = 0;
    }
  }

}

void print_arr(int **a, int N, int M)
{
  int i,j;
  for (i=0; i<N; i++)
  {
    for (j=0; j<M; j++)
      printf("%02d ", a[i][j]);
    printf("\n");
  }
    
}
int main(int argc, char *argv[])
{
  int **a;
  int N = 8;
  int M = 10;
  a = malloc(N*sizeof(int *));
  int counter = 1;
  int i,j;
  for (i=0; i<N; i++)
  {
    a[i] = malloc(M*sizeof(int));
    for (j=0; j<M; j++)
    {
      a[i][j] = counter++;
    }
  }

  a[1][2] = 0;
  a[0][6] = 0;
  a[3][4] = 0;

  print_arr(a, N, M);
  
  zero(a, N, M);
  printf("-----\n");
  print_arr(a, N, M);
}

