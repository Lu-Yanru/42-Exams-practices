#include <unistd.h>

static char alpha_mirror(char c)
{
    if (c >= 'a' && c <= 'z')
        c = 26 - (c - 'a') - 1 + 'a';
    else if (c >= 'A' && c <= 'Z')
        c = 26 - (c - 'A') - 1 + 'A';
    return (c);
}

int main(int argc, char *argv[])
{
    int i;

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    while (argv[1][i])
    {
        argv[1][i] = alpha_mirror(argv[1][i]);
        write(1, &argv[1][i], 1);
        i++;
    }
    write(1, "\n", 1);
}