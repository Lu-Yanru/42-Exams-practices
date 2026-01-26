int ft_isspace(char c)
{
    if (c == ' ' || c == '\f' || c == '\n'
        || c == '\r' ||  c == '\t' || c == '\v')
        return (1);
    else
        return (0);
}

int ft_isbase(char c, int str_base)
{
    int i;
    char *lbase = "0123456789abcdef";
    char *ubase = "0123456789ABCDEF";

    i = 0;
    while (i < str_base)
    {
        if (c == lbase[i] || c == ubase[i])
            return (1);
        i++;
    }
    return (0);
}

int ft_atoi_base(const char *str, int str_base)
{
    int i;
    int sign;
    long n;

    i = 0;
    sign = 1;
    n = 0;
    while (ft_isspace(str[i]) != 0)
        i++;
    if (str[i] == '+' || str[i] == '-')
    {
        if (str[i] == '-')
            sign = -1;
        i++;
    }
    while (ft_isbase(str[i], str_base) != 0)
    {
        if (str[i] >= '0' && str[i] <= '9')
            n = n * str_base + str[i] - '0';
        else if (str[i] >= 'a' && str[i] <= 'z')
            n = n * str_base + str[i] - 'a' + 10;
        else if (str[i] >= 'A' && str[i] <= 'Z')
            n = n * str_base + str[i] - 'A' + 10;
        i++;
    }
    return ((int) n * sign);
}