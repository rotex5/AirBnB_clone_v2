# puppet script that sets up your web servers for the deployment of web_static
include stdlib

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update packages']
}

exec {'create directories':
  command  => '/usr/bin/mkdir -p /data/web_static/releases/test/',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

file { '/data/web_static/shared':
  ensure => 'directory'
  require => Exec['create directories']
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

exec { 'nginx_conf':
  environment => ['data=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sed -i "39i $data" /etc/nginx/sites-enabled/default',
  path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
}

exec { 'restart nginix':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}
