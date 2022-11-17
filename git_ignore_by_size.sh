#/bin/bash
find . -size +99M | cat >> .gitignore
git rm -rf --cached .
git add .

