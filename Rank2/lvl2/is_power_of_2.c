int is_power_of_2(unsigned int n)
{
    int tmp;

    tmp = 1;
    while (tmp <= n)
    {
        if (tmp == n)
            return (1);
        tmp = tmp * 2;
    }
    return (0);
}