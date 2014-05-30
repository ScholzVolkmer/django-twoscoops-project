#!/bin/sh
# save previous vagrant and environment directories
 if [ -z "$1" ]
 then
  echo "Invalid params"
  exit 1
 fi
mv $1/.vagrant .
rm -rf $1
django-admin.py startproject --template=../ -n Vagrantfile,default.rb,metadata.rb,Berksfile,.gitignore -e html $1

# move the directories back
mv .vagrant $1/


cd $1
# remove git submodules information
git init
git add .
git commit -m "Initial commit"
