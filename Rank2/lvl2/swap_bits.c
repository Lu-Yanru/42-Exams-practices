// shift the left half 4 bits to the right (left half becomes 0s)
// and the right half 4 bits to the right (right half becomes 0s)
// and combine them bitwise using |
// (compares each bit position and returns 1 if at least one of the bits is 1.)
unsigned char   swap_bits(unsigned char octet)
{
    return ((octet >> 4) | (octet << 4));
}