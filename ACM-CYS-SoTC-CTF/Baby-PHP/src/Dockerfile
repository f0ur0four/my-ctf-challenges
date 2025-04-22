FROM php:8.2-apache

COPY deploy/php.ini /usr/local/etc/php/php.ini

COPY deploy/index.php /var/www/html/index.php
COPY deploy/flag.txt /var/www/html/flag.txt

RUN chown -R www-data:www-data /var/www/html
