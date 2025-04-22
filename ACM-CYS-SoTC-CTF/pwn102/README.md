[Pwn] pwn102

Time to level up, shall we?

## Attachments

- [pwn102.zip](attachments/pwn102.zip)

## Solution

After running checksec, you'll see that the binary has all mitigations enabled, so neither you can do ret2shellcode, GOT Overwrite, or a basic ret2win (since no win function is provided). But the provided libc is 2.27 of Ubuntu 18 which is pretty old.

In the older versions of LIBC, there are hooks which are basically variables which help in debugging functions like free(), malloc() and realloc(). Whenever malloc or free is called, it checks if the __malloc_hook (for malloc) or __free_hook (for free) variable is not NULL. If true, then it executes the function pointed to by that hook variable before executing malloc/free/realloc and the argument provided to malloc/free is then passed to that function to be executed.

Since the challenge calls both malloc and free, the goal is clear, i.e., to overwrite either free or malloc hook with the address of system. Using the format string, you can leak LIBC address and then calculate the base address of LIBC, from there you can then add the offset of free/malloc hook to get it's address. Now getting the address of system() is easy but we also need to provide the argument "/bin/sh", I didn't spend time doing that, instead I used one gadget. You can think of a one gadget as a line of C code which just calls `execve("/bin/sh", NULL, NULL)`, all you need to do is just overwrite the address of the hook with the address of one gadget and you will get the shell! I didn't try overwriting the malloc hook, and chose to overwrite __free_hook :).

Solver: [solve.py](solve.py)

## Flag

```
STC{u51ng_f0rm47_57r1ng5_70_0v3rwr1t3_h00k5_15_c00l_r1gh7??!!!!}
```