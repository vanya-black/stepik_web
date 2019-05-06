sudo pip3 install --upgrade Django==2.0.0
sudo pip3 install --upgrade gunicorn==19.6.0
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
