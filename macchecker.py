#!/usr/bin/env python

import sys
import gtk
import appindicator

"""
This code is based on the example from here: http://conjurecode.com/create-indicator-applet-for-ubuntu-unity-with-python/
Rewritten Feb 14, 2016 by Michael Harwood.

In Ubuntu 14.04 one has to explicitly `sudo apt-get install python-appindicator` (for python2) to get the `import appindicator` line to work. 

"appindicator" must be imported for the Unity interface

The icons that my computer uses are from: /usr/share/icons/gnome-colors-common/scalable/status
This may change depending on the theme that you use. 

More documentation below from: https://developer.ubuntu.com/api/devel/ubuntu-13.10/python/AppIndicator3-0.1.html

Appindicator Constructors
=========================
 new  (id, icon_name, category)
 new_with_path  (id, icon_name, category, icon_theme_path)

IndicatorStatus
--------------
PASSIVE 0
ACTIVE 1
ATTENTION 2

IndicatorCategory
-----------------
APPLICATION_STATUS 0
COMMUNICATIONS 1 
SYSTEM_SERVICES 2 
HARDWARE 3
OTHER 4

"""


PING_FREQUENCY = 60

"""set up all of the functionality"""
class CheckMAC:
	#permanent MAC addresses here (samples not mine)
	mac_eth0  = '31:17:2b:54:c8:7e'
	mac_wlan0 = '2c:b6:55:22:90:5b' 
	curr_eth0 = '0'
	curr_wlan0 = '0'

	def __init__(self):
		self.ind = appindicator.Indicator("debian-doc-menu", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)

		#you can set the status to various states. Since I have more than two states, I don't use this.
		self.ind.set_status(appindicator.STATUS_ACTIVE)
		#self.ind.set_status(appindicator.STATUS_ATTENTION)

		#icon for active state
		self.ind.set_icon("user-online")
		#icon for attention state
		self.ind.set_attention_icon("new-messages-red")

		self.menu_setup()
		self.ind.set_menu(self.menu)


	def menu_setup(self):
		self.curr_eth0 = open('/sys/class/net/eth0/address').read().strip()
		self.curr_wlan0 = open('/sys/class/net/wlan0/address').read().strip()

		self.menu = gtk.Menu()

		self.mac1_item = gtk.MenuItem('eth0=' + self.mac_eth0)
		self.mac1_item.show()
		self.menu.append(self.mac1_item)

		self.mac2_item = gtk.MenuItem(' now: ' + self.curr_eth0)
		self.mac2_item.show()
		self.menu.append(self.mac2_item)

		separator = gtk.SeparatorMenuItem()
		separator.show()
		self.menu.append(separator)

		self.mac3_item = gtk.MenuItem('wlan0=' + self.mac_wlan0)
		self.mac3_item.show()
		self.menu.append(self.mac3_item)

		self.mac4_item = gtk.MenuItem('  now: ' + self.curr_wlan0)
		self.mac4_item.show()
		self.menu.append(self.mac4_item)

		separator = gtk.SeparatorMenuItem()
		separator.show()
		self.menu.append(separator)

		self.refresh_item = gtk.MenuItem("Refresh")
		self.refresh_item.connect("activate", self.refresh)
		self.refresh_item.show()
		self.menu.append(self.refresh_item)

		self.quit_item = gtk.MenuItem("Quit")
		self.quit_item.connect("activate", self.quit)
		self.quit_item.show()
		self.menu.append(self.quit_item)

	def main(self):
		self.check_mac()
		gtk.timeout_add(PING_FREQUENCY * 1000, self.check_mac)
		gtk.main()


	def refresh(self, widget):
		self.check_mac()

	def quit(self, widget):
		sys.exit(0)

	def check_mac(self):
		count = 0

		# Read eth0 MAC from file and update menu label
		self.curr_eth0 = open('/sys/class/net/eth0/address').read().strip()
		self.mac2_item.get_child().set_label(' now: ' + self.curr_eth0)
		# Read wlan0 MAC from file
		self.curr_wlan0 = open('/sys/class/net/wlan0/address').read().strip()
		self.mac4_item.get_child().set_label('  now: ' + self.curr_wlan0)

		#calculate which icon to show
		if self.curr_eth0 !=  self.mac_eth0:
			count = count + 1
		if self.curr_wlan0 !=  self.mac_wlan0:
			count = count + 2
		#now set the icons (green, yellow, orange, locked

		#DEBUG
		#print 'count =' , count

		if count == 0: self.ind.set_icon("user-online")
		if count == 1: self.ind.set_icon("user-extended-away")
		if count == 2: self.ind.set_icon("update-notifier")
		if count == 3: self.ind.set_icon("locked")
		
		return True


if __name__ == "__main__":
	indicator = CheckMAC()
	indicator.main()


"""
#This is stuff from previous versions ...

		if mac1 ==  mac_eth0:
			self.ind.set_status(appindicator.STATUS_ATTENTION)
		else:
			self.ind.set_status(appindicator.STATUS_ACTIVE)
		return True

	def getmac(self, interface):
		# Return the MAC address of interface
		try:
			str = open('/sys/class/net/%s/address', interface).readline()
		except:
			str = "00:00:00:00:00:00"
		return str[0:17]
		
#==============================================

#!/usr/bin/env python
#import uuid
#print ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
	import re, uuid
	print ':'.join(re.findall('..', '%012x' % uuid.getnode()))
print uuid.getnode()

"""
