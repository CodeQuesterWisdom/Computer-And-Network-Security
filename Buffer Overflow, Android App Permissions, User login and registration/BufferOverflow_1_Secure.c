#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// In this, we use fgets - which is secure version of gets which can limit the length of user input
// to prevent buffer overflow.
// In the same way, we use strncmp - which is secure version of strcmp - which limits the length of input string
// and to the string which it gets compared which prevents buffer overflow
// So, in this root privileges will not be granted to user if it is wrong password

int main(void)
{
    char buff[15];
    int pass = 0;
    int l=0;

    printf("\n Enter the password : \n");
    fgets(buff, 15, stdin);

    if(strncmp(buff, "password",15))
    {
        printf ("\n Wrong Password \n");
    }
    else
    {
        printf ("\n Correct Password \n");
        pass = 1;
    }

    if(pass)
    {
        printf ("\n Root privileges given to the user \n");
    }

    return 0;
}
