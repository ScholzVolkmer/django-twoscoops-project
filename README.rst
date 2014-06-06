========================
vachango: django chef+vagrant project template
========================

General integration of Vagrant, Chef and django project templates. The point of the project is to automate development
routine, needed to start working django project in Vagrant.

Prerequisites
================
- Vagrant (last version)
- Django (if you have multiple python projects or django versions, probably you will need virtualenv) and django-admin.py reachable from future project directory
- Git
- Virtualbox
- Ubuntu 12.04 (server)

Configuring Vagrant and Chef
================
Download Vagrant 1.5.2 (newer versions are not supported by berkshelf plugin, possibly obsolete): http://www.vagrantup.com/download-archive/v1.5.2.html

Install plugins:

- `vagrant plugin install vagrant-omnibus`
- `vagrant plugin install vagrant-berkshelf --plugin-version '>= 2.0.1'`
- for back rsyncing: `vagrant plugin install vagrant-rsync-back`

Remove Berksfile.lock and .vagrant if they are already there somehow.

Start project
================

Copy utils/start_project.sh script somewhere, you want to start the django project.
Execute it :)

`sh start_project.sh {{project_name}}`

Actually it's nothing more than big django startproject command:

        django-admin.py startproject --template=https://github.com/ScholzVolkmer/vachango/archive/develop.zip \
        -n Vagrantfile,Makefile,Vagrantfile_servertest,Berksfile,.gitignore -e html,erb,rst,json,bat,rb,py $1

Make needed editions and then say `vagrant up --provision` to create a vagrant instance.

This takes much time (10-15 min), so get a drink ;)

**Attention**: mysql user name will be the same as project name by default, but due to mysql limits it must be shorter than 16 symbols.

Server
================

* Change database password in `{{project_name}}/settings/<env_name>.py` and `chef/<env_name>.json` to some secret values (and put in repo)
* Change ALLOWED_HOSTS to your host name in `{{project_name}}/settings/<env_name>.py`
* Change domain sites in `{{project_name}}/application/fixtures/initial_data.json` to your domains
* Set raven token if you use sentry in `{{project_name}}/settings/<env_name>.py`
* Install chef-kit with utils/install_chef_kit.sh using sudo. It installs all the binaries needed by chef and chef-kit itself (chef-solo, berkshelf etc)
* Perform berkshelf vendoring:

        berks vendor ./chef/berkshelf

* cd to chef directory and perform chef provisioning with

        sudo chef-solo -c solo.rb -j <env_name>.json

<env_name> is production or staging or whatever.

**Heads up!** Don't forget to change passwords in <env_name>.json to which you want or even disable auto configuration of mysql or other components.

Also here is json job sketch you would create to serve the project

        cd /home/web/{{project_name}}/site/include
        git checkout master
        git stash
        git pull
        git stash pop
        if [ ! -d "./chef/berkshelf" ]; then
           berks vendor ./chef/berkshelf
        fi
        cd chef
        sudo chef-solo -c solo.rb -j <env_name>.json
        cd -
        touch {{project_name}}/{{project_name}}/settings/production.py

Of course your jenkins should be almighty.

If you want to test your server setup you can use Vagrantfile_servertest, which works on the port 8000 and has chef provisioning disabled. You can configure it like it were a server.

Related projects and docs
================
- Vagrant: http://docs.vagrantup.com/v2/. Last releases: http://www.vagrantup.com/downloads.html
- Chef: http://docs.opscode.com/
- Django admin startproject command: https://docs.djangoproject.com/en/dev/ref/django-admin/#startproject-projectname-destination

Misc
================

- Don't forget update vagrant :)
- Start script initializes git repo in the new project directory. Don't forget to set upstream
- Theoretically, after some upcoming changes (for example new python requirements), you just need to perform `vagrant provision`
and vagrant updates the dependencies

Acknowledgements
================

- Forked from django-twoscoops-project
