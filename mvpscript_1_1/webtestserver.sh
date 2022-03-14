#!/bin/bash
# installeer Apache Webserver en PHP
yum install -y httpd mysql PHP
# lab bestanden downloaden
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
# schakel webserver in
chkconfig http on
service httpd start
