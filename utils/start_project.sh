#!/bin/sh
django-admin.py startproject --template=https://github.com/ScholzVolkmer/django-twoscoops-project/archive/develop.zip\
 -n Vagrantfile,default.rb,metadata.rb,Berksfile,.gitignore -e html,erb $1
cd $1
vagrant up
