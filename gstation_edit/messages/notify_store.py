"""
 gstation-edit NotifyStore definition
"""
# this file is part of gstation-edit
# Copyright (C) F LAIGNEL 2009-2017 <fengalin@free.fr>
#
# gstation-edit is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gstation-edit is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gstation_edit.messages.jstation_sysex_event import JStationSysexEvent

class NotifyStore(JStationSysexEvent):
    PROCEDURE_ID = 0x22
    VERSION = 1

    def __init__(self, channel=-1, sysex_buffer=None, prg_nb=-1):
        self.prg_nb = prg_nb

        JStationSysexEvent.__init__(self, channel, sysex_buffer=sysex_buffer)


    def parse_data_buffer(self):
        JStationSysexEvent.parse_data_buffer(self)
        self.prg_nb = self.read_next_bytes(2)


    # Build to send
    def build_data_buffer(self):
        JStationSysexEvent.build_data_buffer(
            self,
            pre_len_data=[self.prg_nb]
        )


    def __str__(self):
        return '%s, prg nb: %d'%(JStationSysexEvent.__str__(self), self.prg_nb)

