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

API:


Uses:
  - moisture, light, touch, buzzer, and button libraries

"""

import moisture as MOIST
import light as LIGHT
import touch as TOUCH
import buzzer as BUZZER
import button as BUTTON

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
    i2c         = busio.I2C(board.SCL_2, board.SDA_2)
    
    def __init__(self,moist="AIN6",light_bus=1,light_address=0x23,touch_bus=i2c,touch_address=0x29,buzzer="P2_1", button="P2_2"):
        """ Initialize variables """
        self.moist      = MOIST.Moisture(moist)
        self.light      = LIGHT.Light(light_bus,light_address)
        self.touch      = TOUCH.Touch(touch_bus,touch_address)
        self.buzzer     = BUZZER.Buzzer(buzzer)
        self.button     = BUTTON.Button(button)
        
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
        
        return notes_nat,notes_sharp
        
    def get_tempo(self):
        light_value     = None
        
        light_value = self.light.get_value()
        
        if light_value < 200:
            tempo = -0.00125 * light_value + 1
        elif light_value < 600:
            tempo = -0.00125 * light_value + 0.75
        elif light_value < 1500:
            tempo = -0.000167 * light_value + 0.25
        else:
            tempo = 0.09
        
        #if light_value < 1250:
        #        tempo = - 0.00072 * (light_value) + 1
        #else:
        #    tempo = 0.09
                
        return tempo
        
    def get_array(self):
        moist_value     = None
        
        notes_nat,notes_sharp = self.note_array()
        
        moist_value = self.moist.get_value()
        if moist_value < MOIST.MIN_TARGET or moist_value > MOIST.MAX_TARGET:
            array = notes_sharp
        else:
            array = notes_nat
            
        return array
            
    def play(self):
        #light_value     = None
        #moist_value     = None
        touch_value_1   = None
        touch_value_2   = None
        tempo           = None
        array           = None
        note            = None
        
        #notes_nat,notes_sharp = self.note_array()
        
        #while True: 
        touch_value_1 = self.touch.get_value() 
            
            #light_value = self.light.get_value()
            #if light_value < 1500:
            #    tempo = - 0.00043 *(light_value) + 0.75
            #else:
            #    tempo = 0.09
            
        tempo = self.get_tempo()
            
            #print("Value = {0}".format(light_value))
            #print("Tempo = {0}".format(tempo))
            
            #moist_value = self.moist.get_value()
            
            #if moist_value < MOIST.MIN_TARGET or moist_value > MOIST.MAX_TARGET:
            #    array = notes_sharp
            #else:
            #    array = notes_nat
            
        array = self.get_array()
        length = len(array)
        quartpoint = int(length/4)
        midpoint = int(length/2)
        tquartpoint = int(3*length/4)
                
        touch_value_2 = self.touch.get_value()
        if touch_value_1 - touch_value_2 != 0:
            if touch_value_2 < -50:
                note = np.random.choice(array[0:quartpoint],size=1)
            elif touch_value_2 < 0:
                note = np.random.choice(array[quartpoint:midpoint],size=1)
            elif touch_value_2 < 50:
                note = np.random.choice(array[midpoint:tquartpoint],size=1)
            elif touch_value_2 < 128:
                note = np.random.choice(array[tquartpoint:-1],size=1)
            #if touch_value_2 > 0:
            #    note = np.random.choice(array[midpoint:-1],size=1)
            #elif touch_value_2 < 0:
            #    note = np.random.choice(array[0:midpoint],size=1)
            else:
                pass
        else:
            pass
            
        self.buzzer.play(note,tempo,False)
        time.sleep(0.01)
            
            #self.buzzer.play(note,tempo,True)
            #time.sleep(0.01)
            
    def stop_button(self):
        return self.button.is_pressed()
    
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
        while True:
            if plant_music.stop_button() == True:
                while True:
                    plant_music.play()
                    if plant_music.stop_button() == True:
                        raise KeyboardInterrupt
                    else:
                        pass
            else:
                pass
            
    except KeyboardInterrupt:
        plant_music.cleanup()
    print("Program Complete")