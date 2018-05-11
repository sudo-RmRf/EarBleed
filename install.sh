#!/bin/bash

mkdir /usr/share/SuperVolume
cp ./* /usr/share/SuperVolume
mv /usr/share/SuperVolume/SuperVolume.desktop /usr/share/applications
#rm -rf "${0%/*}"
