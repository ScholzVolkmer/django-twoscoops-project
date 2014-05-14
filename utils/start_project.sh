#!/bin/sh
django-admin.py startproject --template=https://github.com/ScholzVolkmer/django-twoscoops-project/archive/develop.zip -n Vagrantfile,Berksfile,metadata.rb,default.rb -e html $1
cd $1
vagrant up
vagrant provision
