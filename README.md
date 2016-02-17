# macchecker

A python program that provides a visual indicator to show whether the MAC address has been changed or not. 

-----

### Rationale
When I am in a public place, I often want to use a randomly generated MAC address. The linux program `macchanger -a eth0` (or wlan0) does this. However, when my I close my laptop and open it again, the MAC address tends to get reset to the permanent one. I need a quick and easy way to see if my network connections have anonymous MAC addresses.

### Functionality

I have tried following instructions online about how to automatically generate a random MAC address each time your computer wakes up. However, these ended up disabling my WiFi altogether! So, I still manually run `macchanger`.

This program will show one of four icons depending on the state of the MAC addresses. 

    0 = eth0 is permanent, wlan0 is permanent
    1 = eth0 is random, wlan0 is permanent
    2 = eth0 is permanent, wlan0 is random
    3 = eth0 is random, wlan0 is random

![my icons](https://github.com/salamander2/macchecker/blob/master/macchecker_icons.png)

The indicator icons were chosen for their distinct colours and shapes. (There are a lot of blue and gray icons already on my panel, so I avoided those colours).

Clicking on the icon will show the permanent MAC address as well as the current one. This is just an extra verification that you can do.

Make sure that you run the refresh option if you think something has changed.

### To install this program

* `chmod u+x maccecker.py`
* run the program from wherever you saved it. (e.g /home/salamander2/scripts/macchecker.py)
   * NOTE: run it from the GUI, not from the command line in a terminal
* put this in the list of startup programs for Linux.
* 

### BUGS:
* The program will NOT refresh automatically, so I had to put a Refresh menu option. This works perfectly.
* I don't know how to fix the bug.
