#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i;
    int j;

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    while (argv[1][i])
    {
        if (argv[1][i] == '_')
        {
            i++;
            argv[1][i] = argv[1][i] - 32;
        }
        write(1, &argv[1][i], 1);
        i++;
    }
    write(1, "\n", 1);
}