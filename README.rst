========================
vachango: django chef+vagrant project template
========================

General integration of Vagrant, Chef and django project templates. The point of the project is to automate development
routine, needed to start working django project in Vagrant.

Workflow:
========================
- git gets the development (?) version of this repository and updates all the submodules
- django-admin.py startproject command builds the project using the template structure of the repository and cleans
all the git crumbles (this logics is to change in the future)
- git initializes the repository in the new project, makes initial commit with all the files
- creates vagrant instance with vagrant up
- provisions vagrant with vagrant provision

Prerequisites
================
- Vagrant (last version)
- Django (if you have multiple python projects or django versions, probably you will need virtualenv) and django-admin.py reachable from future project directory
- Git
- Virtualbox
- Ubuntu 12.04 (server)

Start project
================

Copy utils/start_project.sh script somewhere, you want to start the django project.
Execute it :)

`sh start_project.sh <project_name>`

This takes much time (10-15 min), so get a drink ;)

Configuring Vagrant and Chef
================
Download Vagrant 1.5.2 (newer versions are not supported by berkshelf plugin, possibly obsolete): http://www.vagrantup.com/download-archive/v1.5.2.html

Install plugins:

- `vagrant plugin install vagrant-omnibus`
- `vagrant plugin install vagrant-berkshelf --plugin-version '>= 2.0.1'`
- for back rsyncing: `vagrant plugin install vagrant-rsync-back`

Remove Berksfile.lock and .vagrant

start: vagrant up
update: vagrant provision
stop: vagrant provision

Server part
================

* Install chef-kit with utils/install_chef_kit.sh using sudo. It installs all the binaries needed by chef and chef-kit itself (chef-solo, berkshelf etc)
* Perform berkshelf vendoring:

    berks vendor ./chef/berkshelf

* perform chef provisioning with

    sudo chef-solo -c solo.rb -j solo.json

**Heads up!** Don't forget to change passwords in solo.json to which you want or even disable auto configuration of mysql or other components.

Also here is json job sketch you would create to serve the project

    cd /home/web/project_name/site/include
    git checkout master
    git stash
    git pull
    git stash pop
    if [ ! -d "./chef/berkshelf" ]; then
       berks vendor ./chef/berkshelf
    fi
    cd chef
    sudo chef-solo -c solo.rb -j solo.json
    cd -
    touch project_name/project_name/settings/production.py


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
