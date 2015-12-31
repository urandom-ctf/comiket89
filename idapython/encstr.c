#include <stdio.h>

// msg1 = encrypt("mikudayo-", 0x55)
// msg2 = encrypt("fumifumi", 0xaa)
char msg1[] = {0x38,0x3c,0x3e,0x20,0x31,0x34,0x2c,0x3a,0x78,0x00};
char msg2[] = {0xcc,0xdf,0xc7,0xc3,0xcc,0xdf,0xc7,0xc3,0x00};

void decrypt_string(char *s, int k)
{
    while (*s) {
        *s ^= k;
        s++;
    }
}

int main(int argc, char **argv)
{
    decrypt_string(msg1, 0x55);
    puts(msg1);

    decrypt_string(msg2, 0xaa);
    puts(msg2);

    return 0;
}
