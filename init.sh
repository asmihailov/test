sudo ln -sf etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo unlink /etc/nginx/sites-enabled/default
sudo cp etc/nginx.conf /etc/nginx/sites-available/
sudo ln -sf /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf

