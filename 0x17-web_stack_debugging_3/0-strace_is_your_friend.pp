# a puppet script thats able to replace or rewrite a line

$file_path= '/var/ww/html/wp-setting.php'

exec {'replace_line':
    command => "sed -i s/phpp/php/g' $(file_path}",
    path    => ['/bin','/usr/bin']
}
