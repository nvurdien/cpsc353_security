#include <stdio.h>
#include <string.h>
 
int main(int argc, char *argv[])
{
    char buf[64];
 
    strcpy(buf, argv[1]);
    printf("%s\n", buf);
 
    return 0;
}
