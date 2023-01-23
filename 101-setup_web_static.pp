# puppet script that sets up your web servers for the deployment of web_static

exec { 'update':
  command => 'sudo apt-get -y update',
  provier => shell,
}

package { 'nginx':
  ensure => 'installed',
}

service { 'ngnix':
  ensure  => 'running',
  require => Package['nginx'],
}

exec {'create first directory':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  before   => Exec['create second directory'],
}

exec {'create second directory':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  before   => Exec['content into html'],
}

exec {'content into html':
  command  => 'echo "Hello World" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  before   => Exec['symbolic link'],
}

file { '/data/web_static/current':
  ensure => 'link',
  target => /data/web_static/releases/test/,
  before => Exec['nginx config'],
}

exec { 'nginx config':
  environment => ['input=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sed -i "39i $input" /etc/nginx/sites-enabled/default',
  path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
  before      => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  before  => Service['nginx']
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
