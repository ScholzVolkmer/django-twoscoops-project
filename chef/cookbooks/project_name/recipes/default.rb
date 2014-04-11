include_recipe "application"
include_recipe "nginx_conf"

directory "vagrant/shared" do
  owner "vagrant"
  group "vagrant"
  mode '0755'
  recursive true
end

application "{{project_name}}" do
    path "/vagrant"
    owner "vagrant"
    group "vagrant"
    migrate true
    repository node['project']['repository']
    revision node['project']['branch']
    packages ["yui-compressor", "nfs-common", "portmap"]

    django do
        #packages ["redis"]
        requirements "requirements.txt"
        project_name "{{project_name}}"
        #settings_template "settings.py.erb"
        #debug true
        #collectstatic "build_static --noinput"
        #database do
        #    database "packaginator"
        #    engine "postgresql_psycopg2"
        #    username "packaginator"
        #    password "awesome_password"
        #end
    end

    gunicorn do
        app_module :django
        port 5000
        debug true
        project_name "{{project_name}}"
    end
end

nginx_conf_file "{{project_name}}" do
  action :delete
end

nginx_conf_file "{{project_name}}" do
  #root "/vagrant/{{project_name}}/static"
  #site_type :static
  listen "8000"
  locations ({
      '/static/' => {
            'alias' => "/vagrant/{{project_name}}/static/"
        },
      '/' => {
               "proxy_pass" => "http://localhost:5000"
              }
  })
end