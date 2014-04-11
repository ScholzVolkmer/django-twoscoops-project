#!/bin/sh
git clone --depth 1 --no-hardlinks https://github.com/ScholzVolkmer/django-twoscoops-project.git
cd django-twoscoops-project
git submodule update --init --recursive
git submodule foreach git pull origin master
cd ..
django-admin.py startproject --template=django-twoscoops-project -n Vagrantfile,default.rb -e html $1
cd $1
rm .gitmodules
find . -name ".git" -delete
git init
git add .
git commit -m "Initial commit"
vagrant up
vagrant provision
