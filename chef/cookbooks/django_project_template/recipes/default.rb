include_recipe "application"
application "django_project_template" do
    path "/vagrant"
    owner "vagrant"
    group "vagrant"
    migrate true
    repository node['project']['repository']
    revision node['project']['branch']
    #packages ["libpq-dev", "git-core", "mercurial"]

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
end