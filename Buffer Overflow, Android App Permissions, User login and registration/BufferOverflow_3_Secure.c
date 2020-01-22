#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// In this, making sure if position in in range [0-4] inclusive to prevent buffer overflow
int main(void)
{
    char *ptr  = (char*) malloc(5);
    int valid = 0;
    int pos;

    printf("\n Enter the position at which you want to store the character a : \n");
    scanf("%d",&pos);

    if (pos >=0 && pos <5)
    {
      ptr[pos]= 'a';
      printf("Valid : character %c stored at pos %d", ptr[pos], pos);
    }

    else
    {
      printf("\n Invalid input - Position should in the range of [0-4] \n ");
      exit(1);
    }

    return 0;
}
