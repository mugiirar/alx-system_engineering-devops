# Pupppet code for modiffying headers

exec {'update the system':
   owner => shell,
   command => 'sudo apt-get update',
}

exec {'install nginx':
   owner => shell,
   command => 'sudo apt-get install nginx',
}

exec {'html':
   owner => shell,
   command => 'sudo echo "Hello World!" > /usr/share/nginx/html/index.html',
}

exec {'var':
   owner => shell,
   command => 'mkdir -p /var/www/html',
}

exec {'404':
   owner => shell,
   command => 'echo "Ceci n'est pas une page" > /var/www/html/custom_404.html',
}

exec {'default':
   owner => shell,
   command => 'rm /etc/nginx/sites-available/default',
}

exec {'header':
   owner => shell,
   environment => ["HOST=${hostname}"],
   command => 'printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;
    add_header X-Served-By $HOST;
}" > /etc/nginx/sites-available/default',
}

exec {'start app':
   owner => shell,
   command => 'sudo systemctl restart nginx',
}
