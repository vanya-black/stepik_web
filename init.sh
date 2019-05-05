sudo pip3 install --upgrade Django==2.0.0
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/gunicorn stop
#sudo gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_app
sudo /etc/init.d/gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
sudo /etc/init.d/mysql start