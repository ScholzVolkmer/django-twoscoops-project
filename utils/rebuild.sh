#!/bin/bash

 if [ -z "$1" ]
 then
  echo "Invalid params"
  exit 1
 fi
# save previous vagrant and environment directories
mv $1/.vagrant .
rm -rf $1
django-admin.py startproject --template=../ -n Vagrantfile,Makefile,Vagrantfile_servertest,Berksfile,.gitignore\
 -e html,erb,rst,json,bat,rb,py $1

# move the directories back
mv .vagrant $1/
cd $1
