FROM php:8.2-apache

COPY deploy/ /var/www/html/

COPY flag.txt /flag.txt

RUN FLAG_NAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 12) && mv /flag.txt "/flag_${FLAG_NAME}.txt"

RUN chmod -R 755 /var/www/html
