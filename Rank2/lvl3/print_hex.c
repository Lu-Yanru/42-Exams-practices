#include <unistd.h>

int ft_isspace(char c)
{
    if (c == ' ' || c == '\f' || c == '\n'
        || c == '\r' ||  c == '\t' || c == '\v')
        return (1);
    else
        return (0);
}

int ft_atoi(const char *str)
{
    int     i;
    long    n;
    int     sign;

    i = 0;
    n = 0;
    sign = 1;
    while (ft_isspace(str[i]) == 1)
        i++;
    if (str[i] == '+' || str[i] == '-')
    {
        if (str[i] == '-')
            sign = -1;
        i++;
    }
    while (str[i] >= '0' && str[i] <= '9')
    {
        n = n * 10 + str[i] - '0';
        i++;
    }
    return ((int) n * sign);
}

void    ft_puthex(int n)
{
    if (n >= 16)
        ft_puthex(n / 16);
    write(1, &"0123456789abcdef"[n % 16], 1);
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    int n = ft_atoi(argv[1]);
    ft_puthex(n);
}