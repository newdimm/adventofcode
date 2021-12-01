#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void replace_spaces(char *arr, int length)
{
	/* replace single character ' ' with the series of characters {'%', '2', '0'} */
int count;
	int i;
	for (i=0; i<length; i++)
	if (arr[i] == ' ')
			count++;
  
  printf("spaces: %d\n", count);
	
	int new_pos = length + count * 2 - 1;
	int pos = length - 1;

  arr[new_pos+1] = '\0';

  while (pos >= 0)
  {
    printf("%c %d->%d\n", arr[pos], pos, new_pos);
	  if (arr[pos] == ' ')
	  {
		  arr[new_pos] = '0'; new_pos--;
		  arr[new_pos] = '2'; new_pos--;
		  arr[new_pos] = '%';
    }
    else
    {
      arr[new_pos] = arr[pos];
    }
    new_pos --;
    pos --;
  }
}

int main(int argc, char *argv)
{
  const char *s = "Hello to the world of real programmers!!!------------";
  char *arr = malloc(strlen(s) + 1);
  memcpy(arr, s, strlen(s) + 1);
  int length = strlen(arr) - 12;
  printf("<%s> %d %d\n", arr, strlen(arr), length);
  replace_spaces(arr, length);
  printf("<%s>\n", arr);
  return 0;
}
