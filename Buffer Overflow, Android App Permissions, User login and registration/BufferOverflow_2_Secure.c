#include <stdio.h>
#include <string.h>
#include<stdlib.h>


// In this, before accessing buff array to insert a character, first we are checking
// if the position is within buff limits i.e [0-4] inclusive and then inserting if valid.
// If not, we are exiting the program which will not cause buffer overflow
int main(void)
{
    char buff[5];
    int valid = 0;
    int pos;

    printf("\n Enter the position in buff to store the character a : \n");
    scanf("%d",&pos);

    if (pos >=0 && pos <5)
    {
      buff[pos]= 'a';
    }
    else
    {
      printf("\n Invalid input - Position of buffer should in the range of [0-4] \n ");
      exit(1);
    }

    if(valid)
    {
      printf("\n Buffer Overflowed \n");
    }
    return 0;
}
