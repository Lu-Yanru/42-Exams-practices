#include <unistd.h>

void    print_bits(unsigned char octet)
{
    int     i;
    char    bit;

    i = 7;
    while (i >= 0)
    {
        bit = ((octet >> i) & 1) + '0';
        write(1, &bit, 1);
        i--;
    }
}

unsigned char   reverse_bits(unsigned char octet)
{
    int             i;
    unsigned char   res;

    i = 7;
    res = 0;
    // reads from right to left and writes from left to right
    while (i >= 0)
    {
        // shift res left by 1 to the next position
        // extract the right-most bit from octet
        // add that bit to res
        res = (res << 1) | (octet & 1);
        // shift octet right by 1 to process the next bit
        octet >>= 1;
        i--;
    }
    return (res);
}

int main(void)
{
    unsigned char octet = 2;
    print_bits(octet);
    write(1, "\n", 1);
    print_bits(reverse_bits(octet));
}