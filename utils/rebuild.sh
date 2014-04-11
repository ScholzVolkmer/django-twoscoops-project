#!/bin/sh
cd $1
vagrant halt
cd ..
# save previous vagrant and environment directories
 if [ -z "$1" ]
 then
  echo "Invalid params"
  exit 1
 fi
mv $1/.vagrant .
mv $1/shared .
rm -rf $1
django-admin.py startproject --template=../ -n Vagrantfile,default.rb -e html $1

# move the directories back
mv .vagrant $1/


cd $1
# remove git submodules information
git init
git add .
git commit -m "Initial commit"

mv ../shared .
cd $1
vagrant up
vagrant provision
