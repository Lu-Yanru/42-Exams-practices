#include <unistd.h>

int main(int argc, char *argv[])
{
    int i;

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    while (argv[1][i] == ' ' || argv[1][i] == '\f' || argv[1][i] == '\n'
        || argv[1][i] == '\r' ||  argv[1][i] == '\t' || argv[1][i] == '\v')
        i++;
    while (argv[1][i] != ' ' && argv[1][i] != '\f' && argv[1][i] != '\n'
        && argv[1][i] != '\r' &&  argv[1][i] != '\t' && argv[1][i] != '\v'
        && argv[1][i] != '\0')
    {
        write(1, &argv[1][i], 1);
        i++;
    }
    write(1, "\n", 1);
}
