#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   DesafioMundial.py por:
#       Flavio Danesse <fdanesse@gmail.com>
#       Activity Central - CeibalJAM! - Uruguay

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
import sys

import gi
from gi.repository import Gtk
from gi.repository import WebKit

BASEPATH = os.path.abspath(os.path.dirname(__file__))

class DesafioMundial(Gtk.Window):
    
    def __init__(self):
        
        Gtk.Window.__init__(self)
        
        self.set_title("DesafioMundial")
        self.set_icon_from_file(
            os.path.join(BASEPATH, "DesafioMundial.svg"))
            
        self.maximize()
        
        self.add(Navegador())
        
        self.show_all()
        self.realize()
        
        self.connect("destroy", sys.exit)
        
class Navegador(WebKit.WebView):
    
    def __init__(self):
        
        WebKit.WebView.__init__(self)
        
        self.show_all()
        
        self.open(os.path.join(BASEPATH, "juego.swf"))
        self.set_zoom_level(1.0)
        
if __name__ == "__main__":
    
    DesafioMundial()
    Gtk.main()
    