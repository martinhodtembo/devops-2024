#!/bin/bash

sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl status httpd
sudo systemctl enable httpd
sudo cp index.html /var/www/html/
sudo systemctl restart httpd

