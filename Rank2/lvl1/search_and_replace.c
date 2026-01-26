#include <unistd.h>

static int  ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i])
        i++;
    return (i);
}

int main(int argc, char *argv[])
{
    char    *str;
    char    search;
    char    replace;
    int     i;

    if (argc != 4 || ft_strlen(argv[2]) != 1 || ft_strlen(argv[3]) != 1)
    {
        write(1, "\n", 1);
        return (0);
    }
    str = argv[1];
    search = argv[2][0];
    replace = argv[3][0];
    i = 0;
    while (str[i])
    {
        if (str[i] == search)
            write(1, &replace, 1);
        else
            write(1, &str[i], 1);
        i++;
    }
    write(1, "\n", 1);
}