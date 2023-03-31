"""
--------------------------------------------------------------------------
Plant Music
--------------------------------------------------------------------------
License:   
Copyright 2023 - Janie Lim

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make a plant sonification device:  
  - Capacitive Soil Moisture Sensor

Requirements:
  - Hardware:
    - When locked:   Red LED is on; Green LED is off; Servo is "closed"; Display is unchanged
    - When unlocked: Red LED is off; Green LED is on; Servo is "open"; Display is "----"
    - Display shows value of potentiometer (raw value of analog input divided by 8)
    - Button
      - Waiting for a button press should allow the display to update (if necessary) and return any values
      - Time the button was pressed should be recorded and returned
    - User interaction:
      - Needs to be able to program the combination for the “lock”
        - Need to be able to input three values for the combination to program or unlock the “lock”
      - Combination lock should lock when done programming and wait for combination input
      - If combination is unsuccessful, the lock should go back to waiting for combination input
      - If combination was successful, the lock should unlock
        - When unlocked, pressing button for less than 2s will re-lock the lock; greater than 2s will allow lock to be re-programmed

Uses:
  - Libraries developed in class

"""

import moisture as MOIST
import light as LIGHT
import touch as TOUCH
import buzzer as BUZZER
import buzzer_music as MUSIC

import board
import busio
import time
import numpy as np
# import math

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class PlantMusic():
    """ Plant Music Device """
    moist       = None
    light       = None
    touch       = None
    buzzer      = None
    
    def __init__(self, moist="AIN6", light_bus=1, light_address=0x23, touch_bus=None, touch_address=0x29,buzzer="P2_1"):
        """ Initialize variables """
        self.moist      = MOIST.Moisture(moist)
        self.light      = LIGHT.Light(light_bus,light_address)
        self.touch      = TOUCH.Touch(busio.I2C(board.SCL_2, board.SDA_2),touch_address)
        self.buzzer     = BUZZER.Buzzer(buzzer)
        
        self._setup
        
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
        
        # Moisture/
        #   - All initialized by libraries when instanitated
        
        #Light:
        #   - No setup as of 3/23
        
        # Touch: already in __init__
        # i2c = busio.I2C(board.SCL_2, board.SDA_2)
        # touch = Touch(bus=i2c, address=touch_address)
        
    def note_array(self):
        # first vector? has no accidentals, second has only accidentals two scales
        # notes_plain = np.array([31,33,37,41,44,49,55,62,65,73,82,87,98,110]) #14
        # notes_sharps = np.array([31,33,35,37,39,41,44,46,49,52,55,58,62,65,69,73,78,82,87,93,98,104,110,117]) #24
        notes_nat = np.array([220,247,262,294,330,349,392,440,494,523,587,659,698,784])
        notes_sharp = np.array([220,233,247,262,277,294,311,330,349,370,392,415,440,466,494,523,554,587,622,659,698,740,784,831])
        
        return notes_plain,notes_sharps
            
    def testing_moist_light_buzzer(self):
        light_value     = None
        moist_value     = None
        touch_value_1   = None
        touch_value_2   = None
        tempo           = None
        array           = None
        note            = None
        
        notes_nat,notes_sharp = self.note_array()
        
        while True: 
            touch_value_1 = self.touch.get_value() 
            
            light_value = self.light.get_value()
            if light_value < 2500:
                tempo = - 0.00026 *(light_value) + 0.75
            else:
                tempo = 0.09
            
            #print("Value = {0}".format(light_value))
            #print("Tempo = {0}".format(tempo))
            
            moist_value = self.moist.get_value()
            
            if moist_value < MOIST.MIN_TARGET:
                array = notes_sharp
                length = len(array)
                midpoint = int(length/2)
                #print(array)
            elif moist_value > MOIST.MAX_TARGET:
                array = notes_sharp
                length = len(array)
                midpoint = int(length/2)
                #print(array)
            else:
                array = notes_nat
                length = len(array)
                midpoint = int(length/2)
                #print(array)
                
            touch_value_2 = self.touch.get_value()
            if touch_value_1 - touch_value_2 != 0:
                if touch_value_2 > 0:
                    note = np.random.choice(array[midpoint:-1],size=1)
                elif touch_value_2 < 0:
                    note = np.random.choice(array[0:midpoint],size=1)
                else:
                    pass
            else:
                pass
            
            self.buzzer.play(note,tempo,False)
            time.sleep(0.01)
            
            #self.buzzer.play(note,tempo,True)
            #time.sleep(0.01)
    
    def cleanup(self):
        self.buzzer.cleanup()
        
            
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")
    
    # Create instantiation of the lock
    plant_music = PlantMusic()
    
    try:
        plant_music.testing_moist_light_buzzer()
    except KeyboardInterrupt:
        plant_music.cleanup()
    