# correct a misspelled .php suffix
exec { 'fix-wordpress':
  command => "sed -ie 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
