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