#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int x;
    int y;
    char sign;
    int res;

    if (argc != 4)
    {
        printf("\n");
        return (0);
    }
    x = atoi(argv[1]);
    y = atoi(argv[3]);
    sign = argv[2][0];
    if (sign == '+')
        res = x + y;
    else if (sign == '-')
        res = x - y;
    else if (sign == '*')
        res = x * y;
    else if (sign == '/')
        res = x / y;
    else
    {
        printf("\n");
        return (0);
    }
    printf("%d\n", res);
}
