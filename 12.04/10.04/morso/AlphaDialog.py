# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gtk

from morso.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('morso')

class AlphaDialog(gtk.Dialog):
    __gtype_name__ = "AlphaDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated AlphaDialog object.
        """
        builder = get_builder('AlphaDialog')
        new_object = builder.get_object('alpha_dialog')
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called when we're finished initializing.

        finish_initalizing should be called after parsing the ui definition
        and creating a AlphaDialog object with it in order to
        finish initializing the start of the new AlphaDialog
        instance.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)
        self.btn = builder.get_object("btn_ok")
        
        
        self.set_modal(False)

    def ok(self, widget, data=None):
        """The user has elected to save the changes.

        Called before the dialog returns gtk.RESONSE_OK from run().
        """
        pass

    def cancel(self, widget, data=None):
        """The user has elected cancel changes.

        Called before the dialog returns gtk.RESPONSE_CANCEL for run()
        """
        pass
        
    def end_alpha(self, widget):
    	self.hide()
    
#    def show(self):
#    	super(gtk.Window, self).show_all()
	


if __name__ == "__main__":
    dialog = AlphaDialog()
    dialog.show()
    gtk.main()
