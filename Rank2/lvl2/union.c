#include <unistd.h>

int main(int argc, char *argv[])
{
    int     i;
    int     j;
    int    lookup[256];

    if (argc != 3)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    j = 0;
    while (argv[1][i])
    {
        if (lookup[(int) argv[1][i]] != 1)
        {
            lookup[(int) argv[1][i]] = 1;
            write(1, &argv[1][i], 1);
        }
        i++;
    }
    while (argv[2][j])
    {
        if (lookup[(int) argv[2][j]] != 1)
        {
            lookup[(int) argv[2][j]] = 1;
            write(1, &argv[2][j], 1);
        }
        j++;
    }
    write(1, "\n", 1);
}