// Dump of assembler code for function _Z3fooi:
//    1106 <+0>:	push   %rbp
//    1107 <+1>:	mov    %rsp,%rbp
//    110a <+4>:	mov    %edi,-0x14(%rbp)
//    110d <+7>:	movl   $0x2,-0x4(%rbp)
//    1114 <+14>:	mov    -0x14(%rbp),%edx
//    1117 <+17>:	mov    -0x4(%rbp),%eax
//    111a <+20>:	add    %edx,%eax
//    111c <+22>:	mov    %eax,-0x8(%rbp)
//    111f <+25>:	mov    -0x8(%rbp),%eax
//    1122 <+28>:	pop    %rbp
//    1123 <+29>:	ret

int foo(int a)
{
    int b = 2;
    int k = a + b;
    return k;
}

// Dump of assembler code for function main():
//    1124 <+0>:	push   %rbp
//    1125 <+1>:	mov    %rsp,%rbp
//    1128 <+4>:	sub    $0x10,%rsp
// => 112c <+8>:	movl   $0x1,-0x4(%rbp)
//    1133 <+15>:	mov    -0x4(%rbp),%eax
//    1136 <+18>:	mov    %eax,%edi
//    1138 <+20>:	call   0x401106 <_Z3fooi>
//    113d <+25>:	mov    %eax,-0x8(%rbp)
//    1140 <+28>:	mov    $0x0,%eax
//    1145 <+33>:	leave
//    1146 <+34>:	ret
// End of assembler dump.

int main()
{
    int a = 1;
    int c = foo(a);
}
