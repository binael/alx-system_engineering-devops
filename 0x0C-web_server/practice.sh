sudo touch testfile
cat <<EOF | sudo tee ./testfile >> /dev/null
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        return 200 "Hello World!\n";
    }
}
EOF
