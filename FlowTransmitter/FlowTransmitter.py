#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        FlowTransmitter.py
#
#  Project :     EPFL_Industrial_Automation
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      luca.joss$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["FlowTransmitter", "FlowTransmitterClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(FlowTransmitter.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	FlowTransmitter.additionnal_import

# Device States Description
# No states for this device


class FlowTransmitter (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(FlowTransmitter.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	FlowTransmitter.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        FlowTransmitter.init_device(self)
        #----- PROTECTED REGION ID(FlowTransmitter.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(FlowTransmitter.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_flowRate_read = 0.0
        #----- PROTECTED REGION ID(FlowTransmitter.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(FlowTransmitter.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.always_executed_hook

    # -------------------------------------------------------------------------
    #    FlowTransmitter read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_flowRate(self, attr):
        self.debug_stream("In read_flowRate()")
        #----- PROTECTED REGION ID(FlowTransmitter.flowRate_read) ENABLED START -----#
        attr.set_value(self.attr_flowRate_read)
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.flowRate_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(FlowTransmitter.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.read_attr_hardware


    # -------------------------------------------------------------------------
    #    FlowTransmitter command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(FlowTransmitter.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	FlowTransmitter.programmer_methods

class FlowTransmitterClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(FlowTransmitter.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	FlowTransmitter.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'flowRate':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(FlowTransmitterClass, FlowTransmitter, 'FlowTransmitter')
        #----- PROTECTED REGION ID(FlowTransmitter.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	FlowTransmitter.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
