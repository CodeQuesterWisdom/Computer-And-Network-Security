#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// Tn this program, strcpy copies string of given length to buff i.e. restring the input length.
// And so,it prevents buffer overflow which will not rewrite pass and so buffer overflowed is not printed
int main(void)
{
    char buff[15];
    int pass = 0;

    strncpy(buff, "passwordkdsnkldnkndkn",5);
    if(pass)
    {
      printf("buffer overflowed");
    }

    return 0;
}
