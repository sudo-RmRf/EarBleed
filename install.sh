#!/bin/bash

sudo apt install python3-tk -y
mkdir /usr/share/SuperVolume
cp ./* /usr/share/SuperVolume
mv /usr/share/SuperVolume/SuperVolume.desktop /usr/share/applications
chmod +x /usr/share/SuperVolume/uninstall.sh
#rm -rf "${0%/*}"
