#!/bin/bash 
sudo apt install python3 -y
sudo apt install python3-tk -y
sudo mkdir /usr/share/SuperVolume
sudo cp ./*.* /usr/share/SuperVolume/
sudo mv /usr/share/SuperVolume/SuperVolume.desktop /usr/share/applications/SuperVolume.desktop
sudo chmod +x /usr/share/SuperVolume/Supervolume.py
sudo chmod +x /usr/share/svstart.sh
sudo ln -s /usr/share/SuperVolume/svstart.sh /bin/supervolume


