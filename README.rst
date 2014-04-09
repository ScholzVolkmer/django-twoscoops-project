========================
django-twoscoops-project-vagrant-chef
========================

General integration Vagrant, Chef and django project templates. The point of the project is to automate development
tasks, needed to start working django project in Vagrant.

Workflow:
- git gets the development (?) version of this repository and updates all the submodules
- django-admin.py startproject command builds the project using the template structure of the repository and cleans
all the git crumbles (this logics is to change in the future)
- git initializes the repository in the new project, makes initial commit with all the files
- creates vagrant instance with vagrant up
- provisions vagrant with vagrant provision

Prerequisites
================
- Vagrant (last version)
- Bash (lol)
- Django (if you have multiple python projects or django versions, probably you will need virtualenv) and
django-admin.py reachable from future project directory
- Git
- Virtualbox

Start project
================

`sh utils/start_project.sh <project_name>`

Runserver
================

- `cd <project_name>`
- `vagrant ssh`
- `cd /vagrant`
- `source source shared/env/bin/activate`
- `python <project_name>/manage.py runserver 0.0.0.0:8000`

From host check normal `127.0.0.1:8000`. Should show basic template (static files still does not work :()

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

Known Issues
================

- Static files won't served
- Development server does not reload the code on change (gunicorn?)
- Cookbooks won't linked as submodules (currently workarounded)

Acknowledgements
================

- Forked from django-twoscoops-project
- Many thanks to Randall Degges for the inspiration to write the book and django-skel.
