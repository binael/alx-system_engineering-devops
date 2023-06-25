file { '~etc/ssh/ssh_config':
  ensure => present,
  content => "Host *\n
  	PasswordAuthentication no\n
	IdentifyFile ~/.ssh/school"\n,
}
