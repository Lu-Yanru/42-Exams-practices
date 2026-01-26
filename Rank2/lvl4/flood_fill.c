#include "flood_fill.h"

void    fill(char **tab, t_point size, char target, int row, int col)
{
    if (row < 0 || col < 0 || row >= size.y || col >= size.x)
        return ;
    // check if current cell is filled or does not match the target
    if (tab[row][col] == 'F' || tab[row][col] != target)
        return ;
    // mark current cell as filled
    tab[row][col] = 'F';
    // recursively fill neighboring cells
    fill(tab, size, target, row - 1, col); // fill cell above
    fill(tab, size, target, row + 1, col); // fill cell below
    fill(tab, size, target, row, col - 1); // fill cell to the left
    fill(tab, size, target, row, col + 1); // fill cell to the right
}

void  flood_fill(char **tab, t_point size, t_point begin)
{
    char    target;

    target = tab[begin.y][begin.x];
    fill(tab, size, target, begin.y, begin.x);
}

/*int main(void)
{
	char **area;
	t_point size = {8, 5};
	t_point begin = {2, 2};
	char *zone[] = {
		"1 1 1 1 1 1 1 1",
		"1 0 0 0 1 0 0 1",
		"1 0 0 1 0 0 0 1",
		"1 0 1 1 0 0 0 1",
		"1 1 1 0 0 0 0 1",
	};
	area = make_area(zone);
	print_tab(area);
	flood_fill(zone, size, begin);
	putc('\n');
	print_tab(area);
	return (0);
}*/