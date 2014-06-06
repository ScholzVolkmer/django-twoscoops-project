#!/bin/bash
django-admin.py startproject --template=https://github.com/ScholzVolkmer/vachango/archive/develop.zip\
 -n Vagrantfile,Makefile,Vagrantfile_servertest,Berksfile,.gitignore -e html,erb,rst,json,bat,rb,py $1
cd $1

