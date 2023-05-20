# a puppet script thats able to i fix500error when get http method is requested to apache

exec {'replace':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
