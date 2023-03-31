"""
--------------------------------------------------------------------------
Moisture Sensor Driver
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

Moisture Sensor Driver

  This driver is built for capacitive moisture sensors that are connected 
directly to the XXXX (i.e. XXXX)

Software API:

  Moisture(pin)
    - Provide PocketBeagle pin that the moisture sensor is connected

  get_value()
    - Returns the raw ADC value.  Integer in [0, 1023] 

  get_voltage()
    - Returns the approximate voltage of the pin in volts

"""

import Adafruit_BBIO.ADC as ADC 

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

MIN_VALUE       = 0
MAX_VALUE       = 1350
MIN_TARGET      = 880
MAX_TARGET      = 1250  

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

PINS_3V3 = ["AIN6", "AIN5"]
PINS_1V8 = ["AIN0", "AIN1", "AIN2", "AIN3", "AIN4", "AIN7"]

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Moisture():
    """ Moisture Sensor Class """
    pin         = None
    voltage     = None
    
    def __init__(self, pin=None, voltage=1.8):
        """ Initialize variables and set up the moisture sensor """
        if (pin == None):
            raise ValueError("Pin not provided for Moisture()")
        else:
            self.pin = pin
            
        if pin in PINS_3V3:
            self.voltage = 3.3
        else:
            self.voltage = 1.8
            
            if pin not in PINS_1V8:
                print("WARNING:  Unknown pin {0}.  Setting voltage to 1.8V.".format(pin))
                
        # Initialize the hardware components        
        self._setup()
                
    # End def
    
                
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Analog Input
        ADC.setup()
    
    # End def
    
    
    def get_value(self):
        """ 
            Get the value of the Moisture Sensor
            Returns:  Integer in [0, 1023]
        """
        # Read raw value from ADC
        return int(ADC.read_raw(self.pin))

    # End def

    
    def get_voltage(self):
        """ Get the voltage of the pin
        
           Returns:  Float in volts
        """
        return ((self.get_value() / MAX_VALUE) * self.voltage)
    
    # End def    
    
    
    def cleanup(self):
        """Cleanup the hardware components."""
        # Nothing to do for ADC
        pass        
        
    # End def

# End class
    
    
    
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    import time

    print("Moisture Sensor Test")

    # Create instantiation of the moisture sensor
    moist = Moisture("AIN6")

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    print("Use Ctrl-C to Exit")
    
    try:
        while(1):
            # Print moisture sensor value
            print("Value   = {0}".format(moist.get_value()))
            print("Voltage = {0} V".format(moist.get_voltage()))
            time.sleep(1)
        
    except KeyboardInterrupt:
        pass

    print("Test Complete")