#include <stdio.h>

#define DEADCODE                    \
    do {                            \
        asm volatile(               \
            "call 1f;"              \
            "1:"                    \
            "popl %%eax;"           \
            "add $0x6, %%eax;"      \
            "jmp *%%eax;"           \
            ::: "eax"               \
        );                          \
    } while(0);

int main()
{
    DEADCODE;

    puts("mikudayo-\n");

    return 0;
}

