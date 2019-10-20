#!/bin/sh
#sudo ln -sf etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart
#sudo unlink /etc/nginx/sites-enabled/default
sudo cp etc/nginx.conf /etc/nginx/sites-available/nginx.conf
sudo ln -sf /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo gunicorn -c /home/box/web/etc/hello.py hello:app &
sudo gunicorn --bind='0.0.0.0:8000' --pythonpath /home/box/web/ask ask.wsgi:application &
