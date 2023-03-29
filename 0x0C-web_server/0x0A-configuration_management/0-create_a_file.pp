#create a file with specifications

file { '/tmp/school':
    ensure => 'file',
    content => 'i love puppet',
    mode => '0744'
    owner => 'www-data',
    group => 'www-data',
}
