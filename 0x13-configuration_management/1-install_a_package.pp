# install puppet-lint gem
package { 'puppet-lint':
  ensure   => latest,
  provider => 'gem',
}
