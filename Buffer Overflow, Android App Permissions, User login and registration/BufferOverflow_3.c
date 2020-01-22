#include <stdio.h>
#include <string.h>
#include<stdlib.h>


// In this program, buffer overflow is occuring in dynamic memory.
// Using malloc, dynamically allocating 5 blocks [0-4]
// Accessing pos 5 is causing buffer overflow
int main(void)
{
    char *ptr  = (char*) malloc(5);
    int pos;

    printf("\n Enter the position at which you want to store the character a : \n");
    scanf("%d",&pos);

    ptr[pos] = 'a';

    printf("character %c stored at pos %d", ptr[pos], pos);

    return 0;
}
