#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   DesafioMundial.py por:
#       Flavio Danesse <fdanesse@gmail.com>
#       CeibalJAM! - Uruguay

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os
import time
import hulahop
import gtk

from sugar.activity import activity
from sugar import env

from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import StopButton

hulahop.startup(os.path.join(env.get_profile_path(), 'gecko'))
from hulahop.webview import WebView

BASEPATH = os.path.abspath(os.path.dirname(__file__))

class DesafioMundial(activity.Activity):
    
    def __init__(self, handle):
        
        activity.Activity.__init__(self, handle, False)
        
        toolbar = ToolbarBox()
        separator = gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar.toolbar.insert(separator, -1)
        separator.show()
        toolbar.toolbar.insert(StopButton(self), -1)
        
        self.set_toolbar_box(toolbar)
        self.set_canvas(Navegador())
        
        self.show_all()
        self.realize()

class Navegador(WebView):
    
    def __init__(self):
        
        WebView.__init__(self)
        
        self.show_all()
        
        self.load_uri(os.path.join(BASEPATH, "juego.swf"))
    