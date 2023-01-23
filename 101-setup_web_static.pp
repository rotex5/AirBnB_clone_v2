# puppet script that sets up your web servers for the deployment of web_static

exec { 'update':
  provider => shell,
  command => 'sudo apt-get update',
}

package { 'nginx':
  ensure => installed,
}

file { '/data':
  ensure  => 'directory'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Hello world'
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

exec { 'nginx_conf':
  provider => shell,
  environment => ['input=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sed -i "39i $input" /etc/nginx/sites-enabled/default',
}

service { 'nginx':
  ensure => running,
}
