# Plant Music
  
## Building Instructions
To find detailed hardware build instructions, go to [Hackster](www.hackster.io/jclim02/plant-music-ff2cc4). Otherwise, a basic system and power block diagram can be found in docs.

For software, download files from the [software folder](https://github.com/jclim02/ENGI301/tree/main/project_01/software). Additionally, run the following code to install necessary applications:

  sudo apt-get update
  
  sudo apt-get install build-essential python-dev python-setuptools python-smbus -y
  
  sudo apt-get install python-pip python3-pip -y
  
  sudo apt-get install zip -y
  
  sudo pip3 install --upgrade setuptools
  
  sudo pip3 install --upgrade Adafruit_BBIO
  
  sudo pip3 install adafruit-blinka
  
  sudo pip3 install adafruit-circuitpython-bh1750
  
  sudo pip3 install adafruit-circuitpython-cap1188
  


## Operation
The program will automatically boot on power-up. To start program, press the button. To stop, press and hold the button. To restart the program after it has been stopped, you will need to reboot the entire device.
