include_recipe "python"
include_recipe "supervisor"
include_recipe "chef_server_test::default"

directory "/home/vagrant/.virtualenvs" do
  owner "vagrant"
  group "vagrant"
  mode 0777
  action :create
end

python_virtualenv "/home/vagrant/.virtualenvs/env" do
  Chef::Log.info("Virtualenv...")
  owner "vagrant"
  group "vagrant"
  action :create
end

venv_python = "/home/vagrant/.virtualenvs/env/bin/python"
manage_py = "/vagrant/{{project_name}}/manage.py"

python_pip "/vagrant/requirements.txt" do
  Chef::Log.info("Create virtualenv")
  virtualenv "/home/vagrant/.virtualenvs/env"
  action :install_requirements
end

execute "#{venv_python} #{manage_py} syncdb --noinput --migrate" do
  Chef::Log.info("Migration/syncdb")
  user 'vagrant'
  group 'vagrant'
end

execute "#{venv_python} #{manage_py} loaddata /vagrant/{{project_name}}/fixtures/superuser.json" do
  Chef::Log.info("Creating django@django superuser")
  user 'vagrant'
  group 'vagrant'
end

execute "#{venv_python} #{manage_py} collectstatic --noinput" do
  Chef::Log.info("Collectstatic")
  user "vagrant"
  group "vagrant"
end

supervisor_service "runserver" do
  Chef::Log.info("Supervisor runserver...")
  action :enable
  autostart true
  user "vagrant"
  command "#{venv_python} #{manage_py} runserver_plus 0.0.0.0:8000"
  stopsignal "KILL"
  startretries 10
  stopwaitsecs 1
end

template "/home/vagrant/.profile" do
  source "profile.erb"
  mode 0644
  owner "vagrant"
  group "vagrant"
end
