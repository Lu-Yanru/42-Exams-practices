#include <unistd.h>

static int ft_strlen(char *str)
{
    int len;

    len = 0;
    while (str[len])
        len++;
    return (len);
}

static int ft_isspace(char c)
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

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = ft_strlen(argv[1]) - 1;
    while (ft_isspace(argv[1][i]) == 1)
        i--;
    while (i >= 0 && ft_isspace(argv[1][i]) == 0)
        i--;
    i++;
    while (argv[1][i] && ft_isspace(argv[1][i]) == 0)
    {
        write(1, &argv[1][i], 1);
        i++;
    }
    write(1, "\n", 1);
}
