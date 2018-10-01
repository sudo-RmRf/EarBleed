#!/bin/bash 
clear
echo -e "\e[41mSuperVolunme is a GUI front end for Pulse Audio Control which will allow you to increase the volume of your computer past 100%. I made this out of necessity for the ability to make my stock laptop speakers louder in a user friendly way. This software could cause damage to your speakers if used carelessly. By typing "'"y"'" you are accepting that you are responsible for the things you do not me. If you can't own your actions type "'"N"'". SuperVolume allows up to 300% volume, this limit was come to mostly because it sounded good and is in no way based on what is safe for your speakers. Again I take no responsibility for reckless use of this software. "
echo -e "\e[0m"
read -p "" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
  sudo apt install python3 -y
  sudo apt install python3-tk -y
  echo "sudo rm -f /bin/supervolume" > ${PWD}/uninstall.sh
  echo "sudo rm -f /usr/share/applications/SuperVolume.desktop" >> ${PWD}/uninstall.sh
  echo "sudo rm -rf ../SuperVolume" >> ${PWD}/uninstall.sh
  sudo chnod +x ./uninstall.sh 
  echo "Icon=""${PWD}""/icon.ico" >> ${PWD}/SuperVolume.desktop
  sudo chmod +x "${PWD}"/SuperVolume.py
  sudo chmod +x "${PWD}"/svstart.sh
  sudo ln -s "${PWD}"/svstart.sh /bin/supervolume
  sudo cp "${PWD}"/SuperVolume.desktop /usr/share/applications/SuperVolume.desktop
fi

