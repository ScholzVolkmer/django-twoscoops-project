include_recipe "python"
include_recipe "{{project_name}}::default"
include_recipe "apache2"

root = File.absolute_path(File.dirname(__FILE__)) + "/../../../../"
main_user = node['{{project_name}}']['user']
environment = node['{{project_name}}']['environment']

python_virtualenv root + "virtualenv" do
  Chef::Log.info("Virtualenv...")
  owner "#{main_user}"
  group "#{main_user}"
  action :create
end

python_pip root + "requirements.txt" do
  Chef::Log.info("Create virtualenv")
  virtualenv root + "virtualenv"
  action :install_requirements
  user "#{main_user}"
  group "#{main_user}"
end

ENV['APP_SETTINGS'] = "#{environment}"
venv_python = root + "virtualenv/bin/python"
manage_py = root + "{{project_name}}/manage.py"
execute "#{venv_python} #{manage_py} syncdb --noinput --migrate" do
  Chef::Log.info("Migration/syncdb")
  user "#{main_user}"
  group "#{main_user}"
end

web_app "{{project_name}}" do
  server_name "{{project_name}}"
  docroot root
  cookbook "{{project_name}}"
  server_admin "admin@example.com"
  wsgi_script_alias "#{root}{{project_name}}/{{project_name}}/wsgi/#{environment}.py"
  static_alias "#{root}{{project_name}}/static"
  media_alias "#{root}{{project_name}}/media"
  user "#{main_user}"
  log_dir "#{root}logs"
end

execute "#{venv_python} #{manage_py} collectstatic --noinput" do
  Chef::Log.info("Collectstatic")
  user "#{main_user}"
  group "#{main_user}"
end
