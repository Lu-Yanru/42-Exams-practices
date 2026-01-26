#include <unistd.h>

static char rot_13(char c)
{
    char    res;

    if (c >= 'a' && c <= 'z')
        res = (c - 'a' + 13) % 26 + 'a';
    else if (c >= 'A' && c <= 'Z')
        res = (c - 'A' + 13) % 26 + 'A';
    else
        res = c;
    return (res);
}

int main(int argc, char *argv[])
{
    int     i;
    char    c;

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    while (argv[1][i])
    {
        c = rot_13(argv[1][i]);
        write(1, &c, 1);
        i++;
    }
    write(1, "\n", 1);
}