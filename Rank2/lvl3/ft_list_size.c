#include "ft_list.h"

int	ft_list_size(t_list *begin_list)
{
    t_list  *tmp;
    int size;

    size = 0;
    tmp = begin_list;
    while (tmp)
    {
        size++;
        tmp = tmp->next;
    }
    return (size);
}