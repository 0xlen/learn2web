#!/bin/bash

# install apache
sudo apt-get update && sudo apt-get install -y apache2

# install php5 and modules
sudo apt-get install -y php5 libapache2-mod-php5 php5-mcrypt

# install mysql server
sudo apt-get install -y mysql-server libapache2-mod-auth-mysql php5-mysql

# install phpmyadmin
sudo apt-get install -y phpmyadmin

# config phpmyadmin
sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-enabled/phpmyadmin.conf
sudo php5enmod mcrypt
sudo service apache2 reload
