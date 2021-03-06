"""
 gstation-edit CbxParameter definition
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

class CbxParameter(Parameter):

    def __init__(self, parent, name, cc_nb=-1, parameter_nb=-1, max_value=-1,
                 is_sensitive=1, value=0):
         Parameter.__init__(self, parent, name, cc_nb, parameter_nb,
                            is_sensitive, value, max_value=max_value)

    def get_str_value(self):
        if self.widget:
            tree_iter = self.widget.get_active_iter()
            if tree_iter:
                model = self.widget.get_model()
                return model[tree_iter][:1][0]
            else:
                return ''
        else:
            return ''

    def get_widget_name(self):
        return self.name + '-cbx'

    def init_widget(self, gtk_builder):
        Parameter.init_widget(self, gtk_builder)
        if self.widget:
            self.widget.set_active(self.value)
            self.widget.connect('changed', self.handle_changed)

    def handle_changed(self, widget):
        active_item = widget.get_active()
        if active_item != -1:
            self.set_value(active_item)
        # else no active item

    def update_widget(self):
        if self.widget:
            self.widget.set_active(self.value)
