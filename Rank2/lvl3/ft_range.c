#include <stdlib.h>

int     *ft_range(int start, int end)
{
    int *arr;
    int size;
    int i;

    i = 0;
    if (start <= end)
        size = end - start + 1;
    else
        size = start - end + 1;
    arr = malloc(size * sizeof(int));
    while (i < size)
    {
        arr[i] = start;
        if (start <= end)
            start++;
        else
            start--;
        i++;
    }
    return (arr);
}