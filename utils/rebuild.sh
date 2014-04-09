# save previous vagrant and environment directories
mv $1/.vagrant .
mv $1/shared .
rm -rf $1
django-admin.py startproject --template=/home/sergey/PycharmProjects/django-twoscoops-project -n Vagrantfile,default.rb -e html $1

# move the directories back
mv .vagrant $1/


cd $1
# remove git submodules information
rm .gitmodules
rm -rf utils
find . -name ".git" -delete
git init
git add .
git commit -m "Initial commit"

mv ../shared .
