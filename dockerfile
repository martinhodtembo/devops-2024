# Use Red Hat Universal Base Image (UBI)
FROM registry.access.redhat.com/ubi8/ubi:latest

# Install Apache (httpd)
RUN yum -y module enable httpd && \
    yum -y install httpd && \
    yum clean all

# Copy the index.html file from the host to the container
COPY index.html /var/www/html/

# Open port 80
EXPOSE 80

# Start Apache in the foreground
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
