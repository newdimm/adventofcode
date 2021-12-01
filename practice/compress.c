#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compress(char *s)
{
  char buf[17];
  int tail = 0;
  int head = 0;
  char prev = 0;
  int counter = 1;
  while (s[head])
  {
  	if (s[head] == prev)
	  	counter++;
	  else
    {
      if (counter > 2)
      {
        snprintf(buf, 17, "%d", counter);
        memcpy(&s[tail], buf, strlen(buf));
        tail += strlen(buf);
      }
      else if (counter == 2)
      {	
        s[tail++] = prev;
      }

      s[tail] = s[head];
      tail++;
	    counter = 1;
    }
    prev = s[head];
    head++;
  }

  if (counter > 2)
  {
    snprintf(buf, 17, "%d", counter);
    memcpy(&s[tail], buf, strlen(buf));
    tail += strlen(buf);
  }
  else if (counter == 2)
  {	
    s[tail++] = prev;
  }
  s[tail] = 0;
}

int main(int argc, char *argv[])
{
    char *s = "dfhwhfwaabbcccddddddddddddddddddddddddeeffefeftttyyy";
  char *buf;
  
  buf = malloc(strlen(s) + 1);
  memcpy(buf, s, strlen(s));
  buf[strlen(s)] = '\0';
  printf("<%s>\n", buf);
  compress(buf);
  printf("<%s>\n", buf);
  
  return 0;
}