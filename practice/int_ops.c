// no minus, times, devide
// can use additions

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <limits.h>

int mul_int(int a, int b)
{
    int i;
    int result = 0;
    int sign_a = (a >> 31) & 1;
    int sign_b = (b >> 31) & 1;
    int sign_c = sign_a ^ sign_b;

    if (sign_a)
        a = ~(unsigned)a + 1;
    if (sign_b)
        b = ~(unsigned)b + 1;

    printf("(%d) %d * (%d) %d == (%d)\n", sign_a, a, sign_b, b, sign_c);
    for (i=0; i < b; i++)
    {
        result = result + a;
    }
    if (sign_c)
        result = ~result + 1;
    return result;

}

int sub_int(int a, int b)
{
    return a + ~b + 1;
}

int div_int(int a, int b)
{
    int i = 0;
    int sign_a = (a >> 31) & 1;
    int sign_b = (b >> 31) & 1;
    if (sign_a)
        a = ~(unsigned)a+1;
    if (sign_b)
        b = ~(unsigned)b+1;
    int sign_c = sign_a ^ sign_b;

    if (b == 0)
        return sign_c ? INT_MIN : INT_MAX;
    while (a >= b)
    {
        a = sub_int(a,b);
        i++;
    }
    return sign_c ? (~i+1):i;
}


void print_int(int number)
{
}

int main(int argc, char *argv[])
{
    int a = 5, b = 6;
    char op = '*';

    if (argc == 4)
    {
        a = atoi(argv[1]);
        op = argv[2][0];
        b = atoi(argv[3]);
    }

    int result = (op == '-') ? sub_int(a,b):
        (op == '/') ? div_int(a,b) :
        (op == '*') ? mul_int(a,b) : 0;

    printf("%d %c %d == %d\n", a, op, b, result);

    return 0;
}
