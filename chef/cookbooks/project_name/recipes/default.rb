include_recipe "python"
include_recipe "supervisor"


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

python_virtualenv "/vagrant/env" do
  Chef::Log.info("Virtualenv...")
  owner "vagrant"
  group "vagrant"
  action :create
end

python_pip "/vagrant/requirements.txt" do
    
    virtualenv "/vagrant/env"
  action :install_requirements
end

execute "/vagrant/env/bin/python /vagrant/{{project_name}}/manage.py syncdb --noinput --migrate" do
  Chef::Log.info("Migration/syncdb")
  user 'vagrant'
  group 'vagrant'
end

execute "/vagrant/env/bin/python /vagrant/{{project_name}}/manage.py loaddata /vagrant/{{project_name}}/fixtures/superuser.json" do
  Chef::Log.info("Creating django@django superuser")
  user 'vagrant'
  group 'vagrant'
end

supervisor_service "runserver" do
  Chef::Log.info("Supervisor runserver...")
  action :enable
  autostart true
  user "vagrant"
  command "/vagrant/env/bin/python /vagrant/{{project_name}}/manage.py runserver 0.0.0.0:8000"
  autorestart true
end