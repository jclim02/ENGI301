"""
--------------------------------------------------------------------------
Plant Music Draft 1
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

Plant Music Driver

  This driver 
  

Software API:

  ThreadedButton(pin, sleep_time=0.1, active_high=True)
    
    start()
      - Starts the button thread
    
    is_pressed()
      - Return a boolean value (i.e. True/False) on if button is pressed
      - Function consumes no time
    
    get_last_press_duration()
      - Return the duration the button was last pressed

    cleanup()
      - Stops the button so thread can exit
      
    Callback Functions:
      These functions will be called at the various times during a button 
      press cycle.  There is also a corresponding function to get the value
      from each of these callback functions in case they return something.
    
      - set_pressed_callback(function)
        - Excuted every "sleep_time" while the button is pressed
      - set_unpressed_callback(function)
        - Excuted every "sleep_time" while the button is unpressed
      - set_on_press_callback(function)
        - Executed once when the button is pressed
      - set_on_release_callback(function)
        - Executed once when the button is released
      
      - get_pressed_callback_value()
      - get_unpressed_callback_value()
      - get_on_pressed_callback_value()
      - get_on_release_callback_value()      

"""
#import time
#import threading
#import Adafruit_BBIO.GPIO as GPIO

# from buzzer.py
import time
import Adafruit_BBIO.PWM as PWM

# from buzzer_music.py
import sys
#import time
import math
import random
#import buzzer

# for moisture sensor
import board
import analogio

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

#HIGH          = GPIO.HIGH
#LOW           = GPIO.LOW

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# note library from buzzer_music.py
NOTE_B0  = 31
NOTE_C1  = 33
NOTE_CS1 = 35
NOTE_D1  = 37
NOTE_DS1 = 39
NOTE_E1  = 41
NOTE_F1  = 44
NOTE_FS1 = 46
NOTE_G1  = 49
NOTE_GS1 = 52
NOTE_A1  = 55
NOTE_AS1 = 58
NOTE_B1  = 62
NOTE_C2  = 65
NOTE_CS2 = 69
NOTE_D2  = 73
NOTE_DS2 = 78
NOTE_E2  = 82
NOTE_F2  = 87
NOTE_FS2 = 93
NOTE_G2  = 98
NOTE_GS2 = 104
NOTE_A2  = 110
NOTE_AS2 = 117
NOTE_B2  = 123
NOTE_C3  = 131
NOTE_CS3 = 139
NOTE_D3  = 147
NOTE_DS3 = 156
NOTE_E3  = 165
NOTE_F3  = 175
NOTE_FS3 = 185
NOTE_G3  = 196
NOTE_GS3 = 208
NOTE_A3  = 220
NOTE_AS3 = 233
NOTE_B3  = 247
NOTE_C4  = 262
NOTE_CS4 = 277
NOTE_D4  = 294
NOTE_DS4 = 311
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_FS4 = 370
NOTE_G4  = 392
NOTE_GS4 = 415
NOTE_A4  = 440
NOTE_AS4 = 466
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_CS5 = 554
NOTE_D5  = 587
NOTE_DS5 = 622
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_FS5 = 740
NOTE_G5  = 784
NOTE_GS5 = 831
NOTE_A5  = 880
NOTE_AS5 = 932
NOTE_B5  = 988
NOTE_C6  = 1047
NOTE_CS6 = 1109
NOTE_D6  = 1175
NOTE_DS6 = 1245
NOTE_E6  = 1319
NOTE_F6  = 1397
NOTE_FS6 = 1480
NOTE_G6  = 1568
NOTE_GS6 = 1661
NOTE_A6  = 1760
NOTE_AS6 = 1865
NOTE_B6  = 1976
NOTE_C7  = 2093
NOTE_CS7 = 2217
NOTE_D7  = 2349
NOTE_DS7 = 2489
NOTE_E7  = 2637
NOTE_F7  = 2794
NOTE_FS7 = 2960
NOTE_G7  = 3136
NOTE_GS7 = 3322
NOTE_A7  = 3520
NOTE_AS7 = 3729
NOTE_B7  = 3951
NOTE_C8  = 4186
NOTE_CS8 = 4435
NOTE_D8  = 4699
NOTE_DS8 = 4978

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Moisture():
    """ Moisture Sensor """
    pin       = None
    
    def __init__(self, pin):
        self.pin = pin
        
    def read_moisture(self):
        moisture_value = analogio.AnalogIn(board.A1)
        
    #def determine_key(self):
        #if moisture_value is within target range (275-380 or moist_targetMIN and moist_targetMAX)
        # use no accidentals
        # else, use accidentals
        
class Light():
    """ Light Sensor """
    # can I use same variable name across different classes?
    pin       = None
    
    def __init__(self, pin):
        self.pin = pin
        
    #def read_light(self):
      
    #def determine_tempo(self):
      
class Touch():
    """ Capacitive Touch Sensor """
    # can I use same variable name across different classes?
    pin       = None
    
    def __init__(self, pin):
        self.pin = pin
        
    #def read_touch(self):
      
    #def determine_note(self):
      

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")
