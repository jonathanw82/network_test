<h1 align="center">
   <img src="" alt="repoimage"/>
 </h1>
 

# Internet Connection Test
This program was created because my digital jukebox software requires an internet connection to run.
Most times the computer is first booted up, the jukebox software will boot before an internet connection has been established, this will cause a security error and the software will then hang.
Even if a connection is established after the software has booted the security issue will remain.

This program gets around this by booting at startup, opening a command prompt and displaying that it is testing for an internet connection every 2 seconds up to 8 times. 
If a connection is established the program will display that a connection is established then boot the Jukebox software removing the problem of any security issues.
After 8 times of no connection, the program will display, that a there is no internet connection and then close.

After writing the program it was then converted to a .exe file by auto-py-to-exe to the make the program executable on a windows platform.


#### The users goals of this program are:
* Automatically test for an internet connection.
* Only run the desired program if a network connection established..
* Visual representation of what is happening.



#### I think this program gives this to the user because:
* The program automatically runs on startup.
* Only if a connection is detected will the desired program be booted.
* The user can see what is going on in the terminal window.


## Credit:

loop.py
https://docs.python.org/3/howto/sockets.html
https://www.youtube.com/watch?v=H5xpMj_-vAo
https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi

opencmd.py

https://stackoverflow.com/questions/46873212/python-to-close-own-cmd-shell-window-on-exit
