#include <stdio.h>

void foo(int a, int b, int c)
{
    char bufs1[5];
    bufs1[0] = 'A';
    bufs1[1] = 'A';
    bufs1[2] = 'A';
    bufs1[3] = 'A';
    bufs1[4] = 'A';

    char bufs2[10];
    char *r;

    r = bufs1 + 0x15;
    (*r) += 7;
}

int main()
{
    int x;
    x = 0;
    foo(1, 2, 3);
    x = 1;
    printf("x = %d\n", x);
}