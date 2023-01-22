#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
apt-get -y update

dpkg -s nginx 2>/dev/null >/dev/null || sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/  /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

input="\
server {
	location /hbnb_static/ {
		alias /data/web_static/current/;
		autoindex off;
	}
}
"
echo "$input" >> /etc/nginx/sites-available/default

sudo service nginx restart
