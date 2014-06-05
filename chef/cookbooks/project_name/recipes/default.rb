include_recipe "python"
include_recipe "supervisor::vagrant"


apt_package "virtualenvwrapper" do
  action :install
end

apt_package "yui-compressor" do
  action :install
end

apt_package "libmysqlclient-dev" do
  action :install
end

apt_package "ruby-full" do
  action :install
end

apt_package "rubygems" do
  action :install
end

apt_package "libfreetype6-dev" do
  action :install
end

apt_package "libjpeg-dev" do
  action :install
end

apt_package "memcached" do
  action :install
end

apt_package "libmemcached-dev" do
  action :install
end

apt_package "libxml2-dev" do
  action :install
end

apt_package "libxslt-dev" do
  action :install
end

gem_package "sass" do
  action :install
end

apt_package "coffeescript" do
  action :install
end

apt_package "mc" do
  action :install
end

apt_package "vim" do
  action :install
end
