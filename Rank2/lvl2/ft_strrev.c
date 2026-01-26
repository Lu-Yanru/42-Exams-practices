#include <stdio.h>

char    *ft_strrev(char *str)
{
    int     i;
    int     len;
    char    tmp;

    i = 0;
    len = 0;
    while (str[len])
        len++;
    while (i < len / 2)
    {
        tmp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = tmp;
        i++;
    }
    return (str);
}

int	main(void)
{
	char s[] = "Hello World";
	ft_strrev(s);
	printf("%s\n", s);
	return (0);
}
