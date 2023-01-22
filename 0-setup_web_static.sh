#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

dpkg -s nginx 2>/dev/null >/dev/null || sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Hello World" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/  /data/web_static/current

chown -R ubuntu:ubuntu /data/

input="\
server {
	location /hbnb_static/ {
		alias /data/web_static/current/ ;
	}
}
"
echo "$input" >> /etc/nginx/nginx.conf

sudo service nginx restart
