#!/usr/bin/python
# -*- coding: utf-8 -*-
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

class MorseMessage:
	
	morsemap = {
		"a": ".-/",
		"à": ".-/",
		"b": "-.../",
		"c": "-.-./",
		"d": "-../",
		"e": "./",
		"è": "./",
		"é": "./",
		"f": "..-./",
		"g": "--./",
		"h": "..../",
		"i": "../",
		"ì": "../",
		"j": ".---/",
		"k": "-.-/",
		"l": ".-../",
		"m": "--/",
		"n": "-./",
		"o": "---/",
		"ò": "---/",
		"p": ".--./",
		"q": "--.-/",
		"r": ".-./",
		"s": ".../",
		"t": "-/",
		"u": "..-/",
		"ù": "..-/",
		"v": "...-/",
		"w": ".--/",
		"x": "-..-/",
		"y": "-.--/",
		"z": "--../",
		" ": "/",
		"'": "/",
	}


	def __init__(self):
		self.msg = ""
		self.coded = ""
		inv = self.morsemap.copy()
		inv.pop("à")
		inv.pop("è")
		inv.pop("é")
		inv.pop("ì")
		inv.pop("ò")
		inv.pop("ù")
		inv.pop("'")
		self.inversemorsemap = {v:k for k, v in inv.items()}

	def setMessage(self, m):
		self.msg = m
		self.coded = self.codeMessage(m)

	def setCoded(self, c):
		self.coded = c
		self.msg = self.decodeMessage(c)

	def codeMessage(self, m):
		output = ""

		for char in m:
			output += self.morsemap.get(char.lower(), "")		
		output += "//"	
		return output

	def decodeMessage(self, c):
		
		charlist = c.split("/")
		def appendSlash(x): return x+"/"
		charlist = map(appendSlash, charlist)

		output = ""
		for letter in charlist:
			output += self.inversemorsemap.get(letter, "")
		return output

	def lencoded(self):
		return len(self.coded)
			


mymsg = "ciao ciao ciao"
mycoded = "-.-./../.-/---//.../---/-./---//-./../-.-./---/.-../.-///"


#coder = MorseMessage()
#coder.setMessage(mymsg)
#print coder.msg
#print coder.coded
#coder.setCoded(mycoded)
#print coder.msg
#print coder.coded

#print "\a"

