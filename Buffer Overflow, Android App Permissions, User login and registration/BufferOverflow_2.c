#include <stdio.h>
#include <string.h>


// In this program, if array is accessed beyond its size i.e. max pos in buff[5] is 4
// But if we are accessing buff[5] which causes buffer overflow and changes 'valid'
// and so it prints Buffer Overflowed
int main(void)
{
    char buff[5];
    int valid = 0;
    int pos;

    printf("\n Enter the position in buff to store the character a : \n");
    scanf("%d",&pos);

    buff[pos]= 'a';

    if(valid)
    {
      printf("\n Buffer Overflowed \n");
    }
    return 0;
}
