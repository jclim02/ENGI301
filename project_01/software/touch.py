"""
--------------------------------------------------------------------------
Capacitive Touch Sensor Driver
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

Capacitive Touch Sensor Driver

  This driver is built for capacitive touch sensors that are connected 
directly to an i2c bus.

Software API:
    - Touch(pin)
        - get_value(): 
            - returns capacitive touch reading as an integer
  
"""

import board
import busio
from adafruit_cap1188.i2c import CAP1188_I2C

import time

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Touch():
    """ Touch Sensor Class """
    bus     = None
    address = None
    command = None
    
    def __init__(self, bus=None, address=None):
        """ Initialize class variables """
        self.bus     = bus
        self.address = address
        self.command = "/usr/sbin/i2cset -y {0} {1}".format(bus, address)
        
        # Set up sensor
        i2c = busio.I2C(board.SCL_2, board.SDA_2)
        cap = CAP1188_I2C(self.bus)
        
    # End def
    
        
    def get_value(self):
        """ Return capacitive touch raw value as integer """
        
        cap = CAP1188_I2C(self.bus)
        
        raw_sensor1 = cap[1].raw_value
        return int(raw_sensor1)
    
    # End def
    
# End class
        
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    # Initialize
    i2c = busio.I2C(board.SCL_2, board.SDA_2)
    touch = Touch(bus=i2c, address=0x29)
    
    try:
        while True:
            print("Value = {0}".format(touch.get_value()))
            time.sleep(1)
            
    except KeyboardInterrupt:
        pass