#include <stdio.h>
#include <string.h>

// In this, buff length is only 2 and 's' length is more than that.
// So, entire sprintf will store entire s into buffer which causes buffer overflow
// and so valid is changed and buffer overflowed is printed
int main(void)
{
  char buff[5];
  char* s = "abcdefgh";
  int valid = 0;

  sprintf(buff, "String stored = %s", s);
  puts(buff);

  if(valid)
  {
    printf("Buffer Overflowed");
  }
  return(0);
}
