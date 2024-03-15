# Use the official Ubuntu Docker image
FROM ubuntu:latest

# Set environment variable to disable prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists
RUN apt-get update

# Install Apache, PHP, and other necessary packages
RUN apt-get install -y apache2 php libapache2-mod-php python3 wget gcc sudo vim cron rsyslog

# Add user
RUN useradd -m Bob && echo "Bob:VeryS3curEP4ssw0rdz" | chpasswd && adduser Bob sudo

# Limit Bob's sudo access to vi
RUN echo 'Bob ALL=(ALL) NOPASSWD: /usr/bin/vim' > /etc/sudoers.d/bob

# Copy the PHP files into the image
COPY index.html /var/www/html/
COPY login.php /var/www/html/
COPY rce.php /var/www/html/

# Priv Esc Stuff
COPY status.sh /tmp/status.sh
COPY suid.c /home/Bob/suid.c

COPY bob_cron /etc/cron.d/bob_cron
RUN chmod 0644 /etc/cron.d/bob_cron
RUN crontab /etc/cron.d/bob_cron

# Redirect cron output to the Docker log
RUN echo "cron.* /var/log/cron.log" >> /etc/rsyslog.conf

RUN chown Bob:www-data /tmp/status.sh
RUN chown www-data:www-data /tmp
RUN chmod 664 /tmp/status.sh

# Compile the suid.c file & set the suid bit
RUN gcc /home/Bob/suid.c -o /usr/local/bin/suid
RUN chown root:root /usr/local/bin/suid
RUN chmod u+s,u+x /usr/local/bin/suid
RUN rm /home/Bob/suid.c

RUN echo "What are you doing here?!?!" > /var/www/html/totallynotaflag.txt
RUN echo "Bob = Pwnd! >:)" > /home/Bob/flag.txt
RUN echo "R00ted! (⌐■_■)" > /root/flag.txt

# Change the Apache listening port to 8080
RUN sed -i 's/80/8080/g' /etc/apache2/ports.conf /etc/apache2/sites-enabled/000-default.conf

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Start Apache and cron
CMD service cron start && apachectl -D FOREGROUND