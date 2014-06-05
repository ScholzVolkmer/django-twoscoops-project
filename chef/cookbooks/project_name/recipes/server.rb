include_recipe "python"
include_recipe "chef_server_test::default"
include_recipe "apache2"

root = File.absolute_path(File.dirname(__FILE__)) + "/../../../../"

python_virtualenv root + "virtualenv" do
  Chef::Log.info("Virtualenv...")
  owner "jenkins"
  group "jenkins"
  action :create
end

python_pip root + "requirements.txt" do
  Chef::Log.info("Create virtualenv")
  virtualenv root + "virtualenv"
  action :install_requirements
  user "jenkins"
  group "jenkins"
end

ENV['APP_SETTINGS'] = "production"
venv_python = root + "virtualenv/bin/python"
manage_py = root + "chef_server_test/manage.py"
execute "#{venv_python} #{manage_py} syncdb --noinput --migrate" do
  Chef::Log.info("Migration/syncdb")
  user "jenkins"
  group "jenkins"
end

web_app "chef_server_test" do
  server_name "chef_server_test"
  docroot root
  cookbook "chef_server_test"
  server_admin "admin@example.com"
  wsgi_script_alias "#{root}chef_server_test/chef_server_test/wsgi/production.py"
  static_alias "#{root}chef_server_test/static"
  media_alias "#{root}chef_server_test/media"
  user 'jenkins'
  log_dir "#{root}logs"
end

execute "#{venv_python} #{manage_py} collectstatic --noinput" do
  Chef::Log.info("Collectstatic")
  user "jenkins"
  group "jenkins"
end
