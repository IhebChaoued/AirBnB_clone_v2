#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create /data/ if it doesn't exist
sudo mkdir -p /data

# Create /data/web_static/ if it doesn't exist
sudo mkdir -p /data/web_static

# Create /data/web_static/releases/ if it doesn't exist
sudo mkdir -p /data/web_static/releases

# Create /data/web_static/shared/ if it doesn't exist
sudo mkdir -p /data/web_static/shared

# Create /data/web_static/releases/test/ if it doesn't exist
sudo mkdir -p /data/web_static/releases/test

# Create a fake HTML file with simple content
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration with alias
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static {/!b;n;c\alias /data/web_static/current/;' "$nginx_config"

# Restart Nginx
sudo service nginx restart
