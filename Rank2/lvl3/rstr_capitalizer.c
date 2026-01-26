#include <unistd.h>

int ft_isspace(char c)
{
    if (c == ' ' || c == '\f' || c == '\n'
        || c == '\r' ||  c == '\t' || c == '\v')
        return (1);
    else
        return (0);
}

int main(int argc, char *argv[])
{
    int i;
    int j;

    if (argc < 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 1;
    while (i < argc)
    {
        j = 0;
        while (argv[i][j])
        {
            if (argv[i][j] >= 'A' && argv[i][j] <= 'Z'
                && ft_isspace(argv[i][j + 1]) == 0 && argv[i][j + 1] != '\0')
                argv[i][j] = argv[i][j] + 32;
            else if (argv[i][j] >= 'a' && argv[i][j] <= 'z'
                && (ft_isspace(argv[i][j + 1]) != 0 || argv[i][j + 1] == '\0'))
                argv[i][j] = argv[i][j] - 32;
            write(1, &argv[i][j], 1);
            j++;
        }
        write(1, "\n", 1);
        i++;
    }
}