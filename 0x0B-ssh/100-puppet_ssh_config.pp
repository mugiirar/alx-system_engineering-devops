# make configurations using puppet

include stdlib

file_line { 'SSH key use':
  path => /etc/ssh/ssh_config,
  ensure => present,
  line => 'IdentityFile ~/.ssh/school'
}

file_line { 'password reject':
  path => /etc/ssh/ssh_config,
  ensure => present,
  line => 'PasswordAuthentication no',
}
