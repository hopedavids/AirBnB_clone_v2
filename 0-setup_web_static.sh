#!/usr/bin/env bash
# This script contains the deployment script for webserver 
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
#Define variables
link_name="/data/web_static/current"
target_path="/data/web_static/releases/test"
# Check if the symbolic link already exists
if [ -L "$link_name" ]; then
  rm "$link_name"   # delete it if it exists
fi

# Create the symbolic link
ln -s "$target_path" "$link_name"
sudo chown -R ubuntu:ubuntu /data/

#Define variables
config_file="/etc/nginx/sites-available/default"
nginx_service="nginx"

# Update the Nginx configuration file
sudo sed -i 's#^\(\s*\)location /hbnb_static/ {\(.*\)$#\1location /hbnb_static/ {\n\1    alias /data/web_static/current/;\n\1    \2#' $config_file

# Restart Nginx
sudo systemctl restart $nginx_service
