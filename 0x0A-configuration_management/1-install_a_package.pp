#installing a flask package

package {'Flask':
  provider => 'pip3',
  ensure => '2.1.0',
  require  => Package['python3-pip'],
}
