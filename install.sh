#!/bin/bash 
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


