#!/bin/sh

cp -R app/public/ $HOME/DropBoxes/themoneybees/Dropbox/Public/public/
rsync -avc app/public/ yesudeep@assets.themoneybees.in:/var/www/assets/themoneybees.in/public/
