## power.c

執行power.c
```
 gcc power.c
 ./a.exe
```
產生組合語言.s檔
```
gcc -S power.c -o power.s
```

產生目的檔.o檔
```
gcc -c power.c -o power.o
```
將該目的檔反組譯
```
objdump -d power.o
```
```sh
power.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <power>:
   0:	f3 0f 1e fa          	endbr64 
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	89 7d ec             	mov    %edi,-0x14(%rbp)
   b:	89 75 e8             	mov    %esi,-0x18(%rbp)
   e:	c7 45 f8 01 00 00 00 	movl   $0x1,-0x8(%rbp)
  15:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
  1c:	eb 0e                	jmp    2c <power+0x2c>
  1e:	8b 45 f8             	mov    -0x8(%rbp),%eax
  21:	0f af 45 ec          	imul   -0x14(%rbp),%eax
  25:	89 45 f8             	mov    %eax,-0x8(%rbp)
  28:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  2c:	8b 45 fc             	mov    -0x4(%rbp),%eax
  2f:	3b 45 e8             	cmp    -0x18(%rbp),%eax
  32:	7c ea                	jl     1e <power+0x1e>
  34:	8b 45 f8             	mov    -0x8(%rbp),%eax
  37:	5d                   	pop    %rbp
  38:	c3                   	ret    

0000000000000039 <main>:
  39:	f3 0f 1e fa          	endbr64 
  3d:	55                   	push   %rbp
  3e:	48 89 e5             	mov    %rsp,%rbp
  41:	48 83 ec 10          	sub    $0x10,%rsp
  45:	c7 45 f8 02 00 00 00 	movl   $0x2,-0x8(%rbp)
  4c:	c7 45 fc 03 00 00 00 	movl   $0x3,-0x4(%rbp)
  53:	8b 55 fc             	mov    -0x4(%rbp),%edx
  56:	8b 45 f8             	mov    -0x8(%rbp),%eax
  59:	89 d6                	mov    %edx,%esi
  5b:	89 c7                	mov    %eax,%edi
  5d:	e8 00 00 00 00       	call   62 <main+0x29>
  62:	89 c1                	mov    %eax,%ecx
  64:	8b 55 fc             	mov    -0x4(%rbp),%edx
  67:	8b 45 f8             	mov    -0x8(%rbp),%eax
  6a:	89 c6                	mov    %eax,%esi
  6c:	48 8d 05 00 00 00 00 	lea    0x0(%rip),%rax        # 73 <main+0x3a>
  73:	48 89 c7             	mov    %rax,%rdi
  76:	b8 00 00 00 00       	mov    $0x0,%eax
  7b:	e8 00 00 00 00       	call   80 <main+0x47>
  80:	b8 00 00 00 00       	mov    $0x0,%eax
  85:	c9                   	leave  
  86:	c3                   	ret
```
印出該目的檔的表頭
```
objdump -h power.o
```
```sh
power.o:     file format elf64-x86-64

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000087  0000000000000000  0000000000000000  00000040  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000000  0000000000000000  0000000000000000  000000c7  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  0000000000000000  0000000000000000  000000c7  2**0
                  ALLOC
  3 .rodata       0000000c  0000000000000000  0000000000000000  000000c7  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .comment      0000002c  0000000000000000  0000000000000000  000000d3  2**0
                  CONTENTS, READONLY
  5 .note.GNU-stack 00000000  0000000000000000  0000000000000000  000000ff  2**0
                  CONTENTS, READONLY
  6 .note.gnu.property 00000020  0000000000000000  0000000000000000  00000100  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .eh_frame     00000058  0000000000000000  0000000000000000  00000120  2**3
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, DATA

```
