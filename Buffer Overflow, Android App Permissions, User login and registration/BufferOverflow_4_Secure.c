#include <stdio.h>
#include <string.h>
#include <math.h>

// In this, using snprintf - secure version of printf
// which has added length parameter which allows only those many characters of input
// to be stored in buffer which prevents buffer overflow and so Buffer Overflowed is not being printed
int main()
{
    char buffer[5];
    char* s = "abcdefghijk";
    int valid = 0;

    int j = snprintf(buffer, 3, "%s\n", s);

    printf(" Character written to buff is %s \n",buffer);

    if(valid)
    {
      printf("Buffer Overflowed");
    }

    return 0;
}
