# puppet script that renames a file
# Puppet manifest that fix bug in wp-setings.php

exec { 'Rename_file and fix php extension issue':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
