# Install Python3 (Upgrading shells)
RUN sudo apt-get update
RUN sudo apt-get install -y python3

# Use the official PHP Docker image with Apache
FROM php:7.4-apache

# Copy the PHP files into the image
COPY index.html /var/www/html/
COPY login.php /var/www/html/
COPY rce.php /var/www/html/

# Change the Apache listening port to 8080
RUN sed -i 's/80/8080/g' /etc/apache2/ports.conf /etc/apache2/sites-enabled/000-default.conf

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080