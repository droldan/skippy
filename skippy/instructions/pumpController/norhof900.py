# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Jordi Andreu Segura"
__maintainer__ = "Jordi Andreu Segura"
__email__ = "jandreu@cells.es"
__copyright__ = "Copyright 2015, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"
__status__ = "Production"


import PyTango

Attribute('SCPIname',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":SYS:NAME?",
           })

Attribute('SerialNumber',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":SYS:SN?",
           })

Attribute('PumpStatus',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":SYS:STATUS?",
           })

Attribute('Temp',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":MEAS:TEMP?",
           'writeCmd': lambda value: ":TEMP %s" % (value),
           })

Attribute('Flow',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":MEAS:FLOW?",
           'writeCmd': lambda value: ":FLOW %s" % (value),
           })

Attribute('Mode',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":PUMP:MODE?",
           'writeCmd': lambda value: ":PUMP:MODE %s" % (value),
           })

Attribute('Operation',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': ":PUMP:CONTROL?",
           'writeCmd': lambda value: ":PUMP:CONTROL %s" % (value),
           })
