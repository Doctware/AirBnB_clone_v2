#!/usr/bin/env bash
# Setting up my server for deployment

if ! command -v nginx &> /dev/null
then
        sudo apt update
        sudo apt install -y nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "
<html>
<head>
</head>
<body>
<h1>Holberton School</h1>
</body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

# creating an symbolic link

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# updatng ngix configuration
sudo sed -i '/listen 80 default_server/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

echo "done!!"
