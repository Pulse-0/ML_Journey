First clone the repository using

git clone repo_url --> get the url form the github

This created a new folder in the local machine with same name as repo

git branch <branch name> --> creates a new branch
git checkout <branch name> --> load this branch so we will work in this branch

before committing we need to add the files to the repo.
git add .
git add -all
git add <filename>

to remove these files
git rm <filename> -->removes from github and local basically deletes
git rm --cached <filename>  -->file stays in local system but no tracked for github

git commit -m "messae" --> commit the changes
git commit -am "message" --> in this case you no need to add files.

Now we have to push the commits to github.
git -push 