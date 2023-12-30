# version of nginx
package { 'make sure nginx is present':
  ensure => installed,
}

service { 'make sure nginx is running':
  ensure  => running,
  require => Package['nginx'],
}
