sudo /etc//init.d/mysql start
sudo mysql -uroot -e "create database qa character set utf8;"
mysql -uroot -e "grant all privileges on *.* to 'root'@'localhost' with grant option;"
/home/box/web/ask/manage.py makemigrations qa
/home/box/web/ask/manage.py migrate


