# Plant Music
  
## Building Instructions
To find detailed hardware build instructions, go to the [Hackster page](https://www.hackster.io/jclim02/plant-music-ff2cc4). Otherwise, a basic system and power block diagram can be found in docs.

For software, download files from the [software folder](https://github.com/jclim02/ENGI301/tree/main/project_01/software). Additionally, run the following code to install necessary applications:

  - sudo apt-get update
  - sudo apt-get install build-essential python-dev python-setuptools python-smbus -y
  - sudo apt-get install python-pip python3-pip -y
  - sudo apt-get install zip -y
  - sudo pip3 install --upgrade setuptools
  - sudo pip3 install --upgrade Adafruit_BBIO
  - sudo pip3 install adafruit-blinka
  - sudo pip3 install adafruit-circuitpython-bh1750
  - sudo pip3 install adafruit-circuitpython-cap1188

### Implement Auto Boot
In order to make the program automatically boot, do the following steps:
  1. sudo crontab -e
  2. Add in the line "@reboot sleep 30 && bash (run directory path) > (cronlog path) 2>&1" with the appropriate paths
  3. Reboot and test

## Operation
The program will automatically boot on power-up. To start program, press the button. To stop, press and hold the button. To restart the program after it has been stopped, you will need to reboot the entire device.

Place the moisture sensor in the soil, and place a capacitive touch connection (wire) on the plant (or other living thing). 

### Basic Explanation of Drivers
The light sensor driver can return lux readings, which determine the duration that the note will play for (or, the tempo). This tempo is calculated from a piecewise system of linear equations in the plant music driver. The brighter the space, the faster the tempo.
  
The moisture sensor driver can return raw readings, which determine what note array the note will come from. If the moisture reading is within a target range, the returned array will be roughly two octaves of natural notes. If the reading is outside the target range, the returned array will contain accidentals as well, to indicate an unhappy condition :(

The touch sensor driver can return raw readings, which help determine what note will be played. The both range of possible touch values and the moisture-determined note array are divided into four sections, and the touch reading determines from which section the note is randomly chosen. Additionally, the note played will not change if the touch readings do not change.
