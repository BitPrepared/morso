# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Nicola Corti corti.nico@gmail.com
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
from gi.repository import GObject

import logging
logger = logging.getLogger('morse')

from morse_lib import Window
from morse.AboutMorseDialog import AboutMorseDialog

from morse.AlphaDialog import AlphaDialog

from morse.coder import MorseMessage

# See morse_lib.Window.py for more details about how this class works
class MorseWindow(Window):
    __gtype_name__ = "MorseWindow"


    m1 = MorseMessage()
    m2 = MorseMessage()
    m3 = MorseMessage()
    m4 = MorseMessage()

    actual = m1


    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MorseWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMorseDialog
        self.speed = 1000
        self.counter = 0

        self.textMsg = builder.get_object("entryMsg")
        self.codedMsg = builder.get_object("entryCodec")
        self.lblSpeed = builder.get_object("lblSpeed")
        self.lblStatus = builder.get_object("lblStatus")
        self.lblActual = builder.get_object("lblActual")
        self.lblPerc = builder.get_object("lblPerc")

        self.textMsg.set_text(self.m1.msg)
        self.img = builder.get_object("image")
        self.img.set_from_file("/usr/share/morse/media/blank.png")

        self.lblStatus.set_text("- Fermo -")


    def on_btnTraduci_clicked(self, widget):
        self.actual.setCoded(self.codedMsg.get_text())
        self.textMsg.set_text(self.actual.msg.strip())

    def on_btnMsg1_clicked(self, widget):
        self.actual = self.m1
        self.textMsg.set_text(self.m1.msg)
        self.lblActual.set_text("Messaggio: 1")

    def on_btnMsg2_clicked(self, widget):
        self.actual = self.m2
        self.textMsg.set_text(self.m2.msg)
        self.lblActual.set_text("Messaggio: 2")

    def on_btnMsg3_clicked(self, widget):
        self.actual = self.m3
        self.textMsg.set_text(self.m3.msg)
        self.lblActual.set_text("Messaggio: 3")

    def on_mnu_new_activate(self, widget):

        fcd = Gtk.FileChooserDialog("Scegli un file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = fcd.run()
        if (response == Gtk.ResponseType.OK):
            f = open(fcd.get_filename(), 'r')
        fcd.destroy()

        self.actual = self.m4
        self.actual.setMessage(f.read().strip())
        self.textMsg.set_text(self.actual.msg)
        f.close()
    
	def on_btnVia_clicked(self, widget):
        self.lblStatus.set_text("- In Riproduzione -")
        self.play = True
        self.mid = False

        GObject.timeout_add(int(self.speed), self.msgsend)

	def on_btnStop_clicked(self, widget):
      
        self.lblStatus.set_text("- Fermo -")
        self.img.set_from_file("/usr/share/morse/media/wrdend.png")
        self.counter = 0
        self.play = False
        self.mid = False

	def on_btnPause_clicked(self, widget):
       
        self.lblStatus.set_text("- In Pausa -")
        self.play = False


    def msgsend(self):

        print self.counter
        print self.actual.lencoded()
        if (self.play and int(self.counter) < int(self.actual.lencoded())):

            if (self.mid == False):
                self.mid = True
                self.img.set_from_file("/usr/share/morse/media/wrdend.png")
            else:    

                self.mid = False
                if (self.actual.coded[self.counter] == '.'):
                    self.img.set_from_file("/usr/share/morse/media/point.png")
                if (self.actual.coded[self.counter] == '-'):
                    self.img.set_from_file("/usr/share/morse/media/line.png")
                if (self.actual.coded[self.counter] == '/'):
                    self.img.set_from_file("/usr/share/morse/media/wrdend.png")

                self.counter += 1

                self.lblPerc.set_text(str(round(float(self.counter)/float(self.actual.lencoded())*100,2)) + " %")

        else:
            self.play = False
            self.lblPerc.set_text("0")
            self.lblStatus.set_text("- In Pausa -")

        return self.play

    def on_btnAlfabeto_clicked(self, widget):
        dialog = AlphaDialog()
        result = dialog.run()
        dialog.hide()

    def on_scaleSpeed_value_changed(self, widget):
        self.lblSpeed.set_text(str(widget.get_value()))
        self.speed = widget.get_value()

    def on_checkCodec_toggled(self, widget):    
        if (widget.get_active()):
            self.codedMsg.set_visible(True)
        else:
            self.codedMsg.set_visible(False)

    def on_checkMsg_toggled(self, widget):    
        if (widget.get_active()):
            self.textMsg.set_visible(True)
        else:
            self.textMsg.set_visible(False)

    def on_entryMsg_changed(self, widget):
        self.actual.setMessage(widget.get_text())
        if (not(self.codedMsg.get_text().strip() == self.actual.coded.strip())):
            self.codedMsg.set_text(self.actual.coded.strip())
    


        # Code for other initialization actions should be added here.

