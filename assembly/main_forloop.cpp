// Dump of assembler code for function main:
//    1106 <+0>:	push   %rbp
//    1107 <+1>:	mov    %rsp,%rbp
//    110a <+4>:	movl   $0x0,-0x4(%rbp)
//    1111 <+11>:	movl   $0x0,-0x8(%rbp)
//    1118 <+18>:	jmp    0x401122 <main+28>
//    111a <+20>:	addl   $0x1,-0x4(%rbp)
//    111e <+24>:	addl   $0x1,-0x8(%rbp)

//    This is i because this is what we compare.
//    1122 <+28>:	cmpl   $0x9,-0x8(%rbp)
//    1126 <+32>:	jle    0x40111a <main+20>
//    1128 <+34>:	mov    $0x0,%eax
//    112d <+39>:	pop    %rbp
//    112e <+40>:	ret

int main()
{
    int j = 0;

    for (int i = 0; i < 10; i++)
    {
        j++;
    }
}