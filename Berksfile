source "http://api.berkshelf.com"

cookbook 'build-essential'
cookbook 'database'
cookbook 'apache2'
cookbook 'mysql', git: 'https://github.com/ScholzVolkmer/mysql.git'
cookbook 'python', git: 'https://github.com/ScholzVolkmer/python.git'
#cookbook 'python', path: '/home/sergey/PycharmProjects/chef/python'
cookbook 'git', git: 'https://github.com/ScholzVolkmer/git.git'
cookbook 'supervisor', git: 'https://github.com/ScholzVolkmer/supervisor.git'
cookbook 'mysql-databases', git: 'https://github.com/ScholzVolkmer/mysql-databases.git'
cookbook '{{project_name}}', path: 'chef/cookbooks/{{project_name}}/'
