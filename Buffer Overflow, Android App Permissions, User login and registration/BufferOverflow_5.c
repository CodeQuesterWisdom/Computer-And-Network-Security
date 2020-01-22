#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// Tn this program, strcpy copies entire string to buff which exceeds buff capacity 15 and
// causes buffer overflow which rewrite pass and so buffer overflowed is printed
int main(void)
{
    char buff[15];
    int pass = 0;

    strcpy(buff, "passwordkdsnkldnkndkn");
    if(pass)
    {
      printf("buffer overflowed");
    }

    return 0;
}
