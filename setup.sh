sudo apt-get install nginx
sudo apt-get install python3.6
sudo apt-get install python3-pip
sudo apt-get install build-essential
sudo apt-get install python3-dev
sudo pip3 install uwsgi
sudo pip3 install Flask
sudo ln -s `pwd`/config/vs-fib-nginx.conf /etc/nginx/sites-enabled/vs-fib.conf
sudo mkdir /tmp/nginx_cache