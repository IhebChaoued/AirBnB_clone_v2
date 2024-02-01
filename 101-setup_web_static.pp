# Task 0 redo using Puppet

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>
<head>
</head>
<body>
Holberton School
</body>
</html>',
  require => File['/data/web_static/releases/test'],
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test/index.html'],
}

exec { 'chown_web_static':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin'],
  require => File['/data/web_static/current'],
}

file_line { 'nginx_config':
  line  => 'location /hbnb_static { alias /data/web_static/current/; }',
  path  => '/etc/nginx/sites-enabled/default',
  after => 'listen 80 default_server',
  notify => Service['nginx'],
}

# Restart Nginx when the configuration is changed
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File_line['nginx_config'],
}
