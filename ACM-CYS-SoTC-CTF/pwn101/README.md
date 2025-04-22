[Pwn] pwn101

Tired of basic buffer overflows? Same. Let’s go beyond the basics.

## Attachments

- [pwn101.zip](attachments/pwn101.zip)

## Solution

In this challenge, we are given a stack address leak and the stack is executable so we have to ret2shellcode.
In order to leak the stack canary, we can overflow the name until the null byte of the canary is not being overwritten. Once the canary has been leaked, the rest is a simple return2shellcode.

Solver: [solve.py](solve.py)

## Flag

```
STC{l34k1ng_574ck_c00k135_f0r_fun_4nd_pr0f17!!!}
```