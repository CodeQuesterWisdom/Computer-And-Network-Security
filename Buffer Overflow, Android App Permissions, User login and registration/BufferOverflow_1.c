#include <stdio.h>
#include <string.h>


// In this, gets can cause buffer overflow as it doensn't check for user inputted string
// So if user input is more than 15 characters long, it will overflow.
// If entered password is more than 15 characters long, then though it is wrong Password,
// root privileges will be granted to user as pass will get changed

//Note: correct password : password
// This program shows 2 ways of buffer overflow (although I wrote additional 4 ways to show bufferoverflow)
int main(void)
{
    char buff[15];
    int pass = 0;

    printf("\n Enter the password : \n");
    gets(buff);

    if(strcmp(buff, "password"))
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
