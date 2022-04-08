#!/bin/bash
          yum -y install httpd
          systemctl enable httpd
          systemctl start httpd
          echo '<html><h1>Joehoe dit is een WEBSERVER!</h1></html>' > /var/www/html/index.html
