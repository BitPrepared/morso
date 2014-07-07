# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gtk

from morso.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('morso')

class CryptDialog(gtk.Dialog):
    __gtype_name__ = "CryptDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated CryptDialog object.
        """
        builder = get_builder('CryptDialog')
        new_object = builder.get_object('crypt_dialog')
        new_object.finish_initializing(builder)
        
        return new_object

    def finish_initializing(self, builder):
        """Called when we're finished initializing.

        finish_initalizing should be called after parsing the ui definition
        and creating a CryptDialog object with it in order to
        finish initializing the start of the new CryptDialog
        instance.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)
        self.set_default_response(-5)
        self.text = builder.get_object("txtPassword")


    def ok(self, widget, data=None):
        """The user has elected to save the changes.

        Called before the dialog returns gtk.RESONSE_OK from run().
        """
        if (self.text.get_text() == "marrano"):
        	self.response(gtk.RESPONSE_OK)
        else:
        	self.response(gtk.RESPONSE_CANCEL)


    def cancel(self, widget, data=None):

        pass


if __name__ == "__main__":
    dialog = CryptDialog()
    dialog.show()
    gtk.main()
