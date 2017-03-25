# kill a process called 'killmenow'
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
