#include <unistd.h>

int main(int argc, char *argv[])
{
    int i;
    int j;
    int repeat;

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    while (argv[1][i])
    {
        j = 0;
        if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
            repeat = argv[1][i] - 'a' + 1;
        else if (argv[1][i] >= 'A' && argv[1][i] <= 'Z')
            repeat = argv[1][i] - 'A' + 1;
        else
            repeat = 1;
        while (j < repeat)
        {
            write(1, &argv[1][i], 1);
            j++;
        }
        i++;
    }
    write(1, "\n", 1);
}