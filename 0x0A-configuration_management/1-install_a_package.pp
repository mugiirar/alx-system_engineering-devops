#installing a flask package

package {'flask':
  provider => 'pip3',
  ensure => '2.1.0',
}
