#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int check_palindrom_perm(char *s)
{
// ignore case
// ignore non-letters
int size = 'z' - 'a': + 1;
int *counters = malloc(size * sizeof(int));
memset(counters, 0, size * sizeof(int));
int i;
for (i=0; s[i] != '\0'; s++)
{
	int index;

	if (s[i] >= 'a' && s[i] <= 'z')
		index = s[i] - 'a';
	else if (s[i] >= 'A' && s[i] <= 'Z')
		index = s[i] - 'A';
	else
		continue;
counters[index]++;
}

int odds = 0;
int evens = 0;
for (i=0; i < size; i++)
{
	if ((counters[i] % 2) == 0)
		evens++;
	else
		odds++;
}
free(counters);
return odds <= 1;
}


int main(int argc, char*argv[])
{
	char *s = "Tact Coa";
	printf("%s: %d\n", s, check_palindrom_perm(s));

	s = "Tact Coaa";
	printf("%s: %d\n", s, check_palindrom_perm(s));
return 0;

}
