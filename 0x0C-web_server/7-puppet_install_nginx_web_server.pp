# Install Nginx web server (w/ Puppet)

# install NGINX

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location = /redirect_me {
        return 301 https://google.com;
    }
}
',
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}
