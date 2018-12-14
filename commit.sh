#!/bin/sh
TMP=`mktemp -d`
NAME="Travis CI"
EMAIL="volltin@live.com"

cp items.json ${TMP}
cd ${TMP}
git init

# config git
git config user.name ${NAME}
git config user.email ${EMAIL}

git add .
git commit -m "Update files"

git push -f "https://${GH_TOKEN}@${GH_REF}" master:json

rm -rf ${TMP}