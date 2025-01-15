#include <stdio.h>
#include <limits.h> // Para obtener los valores máximos de los tipos de datos

int main() {
    // Integer Overflow con int
    int int_max = INT_MAX;
    printf("Valor máximo de int: %d\n", int_max);
    printf("int_max + 1: %d (Overflow)\n\n", int_max + 1);

    // Integer Overflow con unsigned int
    unsigned int uint_max = UINT_MAX;
    printf("Valor máximo de unsigned int: %u\n", uint_max);
    printf("uint_max + 1: %u (Overflow)\n\n", uint_max + 1);

    // Integer Overflow con short
    short short_max = SHRT_MAX;
    printf("Valor máximo de short: %d\n", short_max);
    printf("short_max + 1: %d (Overflow)\n\n", short_max + 1);

    // Integer Overflow con long
    long long_max = LONG_MAX;
    printf("Valor máximo de long: %ld\n", long_max);
    printf("long_max + 1: %ld (Overflow)\n\n", long_max + 1);

    // Integer Overflow con unsigned short
    unsigned short ushort_max = USHRT_MAX;
    printf("Valor máximo de unsigned short: %u\n", ushort_max);
    printf("ushort_max + 1: %u (Overflow)\n\n", ushort_max + 1);

    // Integer Overflow con long long
    long long long_long_max = LLONG_MAX;
    printf("Valor máximo de long long: %lld\n", long_long_max);
    printf("long_long_max + 1: %lld (Overflow)\n\n", long_long_max + 1);

    return 0;
}
