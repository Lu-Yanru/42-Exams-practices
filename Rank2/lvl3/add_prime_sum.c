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

void    ft_putnbr(int n)
{
    if (n > 9)
        ft_putnbr(n / 10);
    write(1, &"0123456789"[n % 10], 1);
}

int is_prime(int n)
{
    int i;

    i = 2;
    if (n <= 1)
        return (0);
    if (n == 2)
        return (1);
    while (i < n)
    {
        if (n % i == 0)
            return (0);
        i++;
    }
    return (1);
}

int main(int argc, char *argv[])
{
    int n;
    int i;
    int sum;

    if (argc != 2 || ft_atoi(argv[1]) <= 1)
    {
        write(1, "0\n", 2);
        return (0);
    }
    n = ft_atoi(argv[1]);
    i = 2;
    sum = 0;
    while (i <= n)
    {
        if (is_prime(i) != 0)
            sum = sum + i;
        i++;
    }
    ft_putnbr(sum);
    write(1, "\n", 1);
}