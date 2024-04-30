#!/usr/bin/env bash
# Puppet configuration of custom HTTP Header
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}
file_line { 'a':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=VvgHfqXHS-8&list=RDVvgHfqXHS-8&index=1 permanent;',
  require => Package['nginx'],
}
file_line { 'b':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}
file { '/var/www/html/index.html':
  content => 'Hello GOD!',
  require => Package['nginx'],
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
