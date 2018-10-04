#!/bin/bash 
clear
echo -e "\e[41mEarBleed is a GUI front end for Pulse Audio Control which will allow you to increase the volume of your computer past 100%. I made this out of necessity for the ability to make my stock laptop speakers louder in a user friendly way. This software could cause damage to your speakers if used carelessly. By typing "'"y"'" you are accepting that you are responsible for the things you do not me. If you can't own your actions type "'"N"'". EarBleed allows up to 300% volume, this limit was come to mostly because it sounded good and is in no way based on what is safe for your speakers. Again I take no responsibility for reckless use of this software. "
echo -e "\e[0m"
read -p "" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
  sudo apt install python3 -y
  sudo apt install python3-tk -y
  echo "sudo rm -f /bin/earbleed" > ${PWD}/uninstall.sh
  echo "sudo rm -f /usr/share/applications/earbleed.desktop" >> ${PWD}/uninstall.sh
  echo "sudo rm -rf ${PWD}" >> ${PWD}/uninstall.sh
  sudo chmod +x ./uninstall.sh 
  echo "Icon=""${PWD}""/icon.ico" >> ${PWD}/earbleed.desktop
  sudo chmod +x "${PWD}"/earbleed.py
  echo "#!/bin/bash" > ${PWD}/ebstart.sh
  echo "python ${PWD}/earbleed.py" >> ${PWD}/ebstart.sh
  sudo chmod +x "${PWD}"/ebstart.sh
  sudo ln -s "${PWD}"/ebstart.sh /bin/earbleed
  sudo cp "${PWD}"/earbleed.desktop /usr/share/applications/earbleed.desktop
fi

