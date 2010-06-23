""" 
    This file is part of OpenHelbreath.

    OpenHelbreath is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenHelbreath is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with OpenHelbreath.  If not, see <http://www.gnu.org/licenses/>.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import warnings
warnings.filterwarnings("ignore")

import sys, re
from LoginServer import CLoginServer
from Frontend import GUI

class Console:
	@staticmethod
	def Print(text):
		print text

def main():
	cfg_frontend = re.compile("frontend\s+=\s+(\w+)").findall(open("LServer.cfg", "rb").read())
	cfg_frontend = cfg_frontend[0].lower() in ["on", "enabled", "1", "true"] if cfg_frontend else False
	Print = Console.Print
	interface = None
	if cfg_frontend:
		print "Init gui..."
		interface = GUI()
		interface.start()
		Print = interface.AddLog
		
	Print("OpenHelbreath Login Server experimental") # Last stable revision
	Print("Copyright (C) 2009-2010 by openhelbreath team")
	Print("This program comes with ABSOLUTELY NO WARRANTY.")
	Print("This is free software, and you are welcome to redistribute it under certain conditions.") 
	Print("")
		
	Server = CLoginServer()
	Server.GUI = interface
	if interface:
		interface.LoginServer = Server
		
	if not Server.DoInitialSetup():
		Print("(!) Stopped!")
		del Server
		return False
	
	if not Server.InitServer():
		del Server
		return False
	
	if interface:
		return
	
	while True:
		try:
			q = raw_input(">>> ")
		except:
			sys.exit(1)
		if q != "":
			Server.CommandHandler(q)
	
if __name__ == '__main__':
	main()
