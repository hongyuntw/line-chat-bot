
msg="update at $(date)"

if [ -n "$*" ]; then
	msg="$*"
fi

git add .
git commit -m "$msg"
git push origin master

# git checkout heroku
# git merge master
# rm .gitignore
# touch .gitignore
# echo "__pycache__/" > .gitignore
# git add .
# git commit -m "$msg"

# git push heroku master