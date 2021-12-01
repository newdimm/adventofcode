#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void rotate(int **a, int N)
{
	int temp;
  int i,j;
  
  for (i=0; i<N/2; i++)
  {
    for (j=i; j<N-i-1; j++)
    {
      temp = a[j][i];
      a[j][i] = a[N-i-1][j];
      a[N-i-1][j] = a[N-j-1][N-i-1];
      a[N-j-1][N-i-1] = a[i][N-j-1];
      a[i][N-j-1] = temp;
    }
  }
}

void print_arr(int **a, int N)
{
  int i,j;
  for (i=0; i<N; i++)
  {
    for (j=0; j<N; j++)
      printf("%02d ", a[i][j]);
    printf("\n");
  }
    
}
int main(int argc, char *argv[])
{
  int **a;
  int N = 5;
  a = malloc(N*sizeof(int *));
  int counter = 0;
  int i,j;
  for (i=0; i<N; i++)
  {
    a[i] = malloc(N*sizeof(int));
    for (j=0; j<N; j++)
    {
      a[i][j] = counter++;
    }
  }
  print_arr(a, N);
  rotate(a, N);
  printf("-----\n");
  print_arr(a, N);
}

