sudo /etc//init.d/mysql start
sudo mysql -uroot -e "create database qa character set utf8;"
mysql -uroot -e "grant all privileges on qa.* to 'box'@'localhost' with grant option;"
/home/box/web/ask/manage.py makemigrations
/home/box/web/ask/manage.py migrate


