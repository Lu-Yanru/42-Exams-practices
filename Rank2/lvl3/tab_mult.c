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

static void ft_putnbr(int num)
{
    if (num > 9)
        ft_putnbr(num / 10);
    write(1, &"0123456789"[num % 10], 1);
}

int main(int argc, char *argv[])
{
    int i;
    int n;
    int res;

    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 1;
    n = ft_atoi(argv[1]);
    while (i <= 9)
    {
        res = i * n;
        ft_putnbr(i);
        write(1, " x ", 3);
        ft_putnbr(n);
        write(1, " = ", 3);
        ft_putnbr(res);
        write(1, "\n", 1);
        i++;
    }
}
