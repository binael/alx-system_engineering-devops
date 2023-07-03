# Automates installation and configuration of nginx

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content =>
"server {
		listen 80 default_server;

        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

        listen [::]:80 default_server;

        root /var/www/html;

		error_page 404 /custom_404.html;


        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
				add_header X-Served-By \$(hostname);
                try_files \$uri \$uri/ =404;
        }
}"
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  require   => Package['nginx'],
}
