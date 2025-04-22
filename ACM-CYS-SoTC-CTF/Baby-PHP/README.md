# [Web] Baby PHP

It wouldn’t be a CTF without a baby challenge, now would it?

## Attachments

- [baby-php.zip](attachments/baby-php.zip)

## Solution (Intended)

The app accepts a POST parameter "baby" which is then passed down to eval(), but before doing that it checks if whether our input contains alphanumeric characters or not. So our goal is to somehow get the flag using only symbols. In PHP, you can xor two characters or even strings like this:

```php
"(#(" ^ "\\[\\" # This will result in txt
```

So, you can write a script to iterate over a list of valid characters and try doing an XOR b/w them to see if they yield a valid character or not. I have created a script for generating the payload which you can find [here](gen.py).

Now, all you need to do is just give that code to the server and the server will run it.

Many functions are disabled so you can't execute system code but file_get_contents() is available, you can use that to read the flag but still you won't get the flag. The server stores the output in a variable and checks if it contains the flag format or not. It can be easily bypassed by converting the flag's contents into a hex or using substr to skip the flag format.

Here's my solver script which will send the following to the server for reading the flag and then will convert it back to ASCII:

```php
bin2hex(file_get_contents("flag.txt")) # This is in obfuscated form in the solution script
```

Solver: [solve.py](solve.py)

## Unintended Solution

When the CTF was about to end, one of the teams told me their solution for this challenge which was completely unintended.

FYI, I forgot to move the flag to / :)))

So, you can get the flag by simply visiting `http://ip:port/flag.txt`.

Since the CTF was about to end, I didn't release a revenge version :(.

## Flag

```
STC{b45h_gl0b_1nj3c710n_v14_f1l3_upl04d_g035_brrrrrrr}
```