#include <unistd.h>

int ft_strlen(char *str)
{
    int len;

    len = 0;
    while (str[len])
        len++;
    return (len);
}

int main(int argc, char *argv[])
{
    int i;
    int j;
    int len;

    if (argc != 3)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    j = 0;
    while (argv[1][i])
    {
        if (argv[1][i] != argv[2][j])
        {
            j++;
            if (argv[2][j] == '\0')
                break ;
            continue ;
        }
        i++;
    }
    len = ft_strlen(argv[1]);
    if (argv[2][j] == argv[1][len - 1])
        write(1, argv[1], len);
    write(1, "\n", 1);
}
