# puppet script that sets up your web servers for the deployment of web_static

exec { 'update':
  provider => shell,
  command  => 'sudo apt-get update',
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

exec { 'give user_group permissions':
  provider => shell,
  command => 'sudo chown -R ubuntu:ubuntu /data/'
}

exec { 'configuring default file':
  provider    => shell,
  environment => ['input=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sudo sed -i "38i $input" /etc/nginx/sites-enabled/default',
}

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
