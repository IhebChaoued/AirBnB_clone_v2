#!/usr/bin/env bash
# Install Nginx if not already installed

if [ ! -x /usr/sbin/nginx ]
then
	sudo apt-get update
	sudo apt-get upgrade -y
	sudo apt-get install -y nginx
	sudo service nginx start
fi

sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo "<html>
<head>
</head>
<body>
Holberton School
</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
