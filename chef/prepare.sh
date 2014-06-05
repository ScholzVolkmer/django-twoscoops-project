#!/bin/bash

# This runs as root on the server
chef_binary=/usr/local/bin/chef-solo

if ! test -f "$chef_binary"; then
	export DEBIAN_FRONTEND=noninteractive
	# Upgrade headlessly (this is only safe-ish on vanilla systems)
	apt-get dist-upgrade
	apt-get update
	apt-get install -y ruby1.9.1 ruby1.9.1-dev make g++ autoconf git
	wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chefdk_0.1.0-1_amd64.deb
	dpkg -i chefdk_0.1.0-1_amd64.deb
	rm chefdk_0.1.0-1_amd64.deb
fi
