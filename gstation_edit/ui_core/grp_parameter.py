"""
 gstation-edit GrpParameter definition
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

from gstation_edit.ui_core.parameter import Parameter

class GrpParameter(Parameter):
    def __init__(self, parent, name, is_active=1):
         Parameter.__init__(self, parent, name, cc_nb=-1, parameter_nb=-1,
                            is_sensitive=is_active)
         self.parameters = dict()

    def get_widget_name(self):
        # no widget here, just a group
        pass

    def get_widget_label_name(self):
        # no widget here, just a group
        pass

    def init_widget(self, gtk_builder):
        for parameter in self.parameters.values():
            parameter.init_widget(gtk_builder)

    def set_sensitive(self, is_sensitive):
        for parameter in self.parameters.values():
            parameter.set_sensitive(is_sensitive)
        self.is_sentitive = is_sensitive

    def send_parameter_value(self, parameter):
        self.set_value(parameter.value)

    def update_widget(self):
        for parameter in self.parameters.values():
            if self.value == parameter.value:
                parameter.set_active(True)
            else:
                parameter.set_active(False)

    def add_parameter(self, parameter):
        if len(self.parameters) == 0:
            self.parameter_nb = parameter.parameter_nb
            self.cc_nb = parameter.cc_nb
            self.value = parameter.value
        self.parameters[parameter.name] = parameter
