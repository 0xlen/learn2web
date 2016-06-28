#!/bin/bash

# install apache
sudo apt-get update && sudo apt-get install apache2

# install mysql server
sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql

# install php5 and modules
sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt

# install phpmyadmin
sudo apt-get install phpmyadmin
