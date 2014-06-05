#!/bin/bash
sudo utils/install_chef_kit.sh
berks vendor ./chef/berkshelf
sudo chef-solo -c ./chef/solo.rb -j ./chef/development.json
