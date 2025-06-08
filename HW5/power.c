#include <stdio.h>

int power(int base, int exp) {
    int result = 1;
    for(int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    int b = 2, e = 3;
    printf("%d^%d = %d\n", b, e, power(b, e));
    return 0;
}
