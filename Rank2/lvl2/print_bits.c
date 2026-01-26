#include <unistd.h>

void    print_bits(unsigned char octet)
{
    int     i;
    char    bit;

    // 1 btye = 8 bits
    i = 7;
    // loop from the right-most position
    while (i >= 0)
    {
        // shift all bits in octet to the right by i position
        // so that the bit to be printed out is at the right-most position.
        // Isolate the right-most bit.
        // convert into character.
        // Because we are shifting from the right-most position,
        // we are printing starting from the left-most position.
        bit = ((octet >> i) & 1) + '0';
        write(1, &bit, 1);
        i--;
    }
}

int main(void)
{
    unsigned char octet = 2;
    print_bits(octet);
}