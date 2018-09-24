#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y install nginx
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
sudo apt-get -y install build-essential
sudo apt-get -y install python3-dev
sudo apt-get -y install uwsgi
sudo apt-get -y install uwsgi-plugin-python3
sudo pip3 install Flask
sudo ln -s `pwd`/config/vs-fib-nginx.conf /etc/nginx/sites-enabled/vs-fib.conf
sudo mkdir /tmp/nginx_cache
sudo mkdir /var/log/vs-fib/
sudo pip3 install pytest
sudo pip3 install pytest-flask