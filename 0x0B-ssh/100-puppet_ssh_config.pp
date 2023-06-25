# Replace or create lines for client configuration

include stdlib

file_line { 'password_change':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'identify_file':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => '    IdentifyFile ~/.ssh/school',
  replace  => true,
}
