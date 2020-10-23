<h1 align="center">
   <img src="https://github.com/jonathanw82/network_test/blob/main/images/repoimage.jpg" alt="repoimage"/>
 </h1>
 

# Internet Connection Test
This program was created because my digital jukebox software requires an internet connection to run.
Most times after the computer is first booted, the jukebox software will boot before an internet connection has been established, this will cause a security error and the software will then hang.

Even if a connection is established after the software has booted the security issue will remain.

This program gets around this, by booting at startup, opening a command prompt, displaying that it is testing for an internet connection. It will then test the connection 
every 2 seconds up to 8 times.

In the meantime, if an internet connection is detected, the program will display connection established, then boot the Jukebox software removing the problem of any security issues.

After 8 times if a connection is not detected, the program will display, no internet connection and then reboot the computer.

After writing the program it was then converted to a (.exe) file, by auto-py-to-exe to make the program easily executable on a windows platform.
##

Originally I added a file called opencmd.py that opened a Windows command prompt and started the loop.exe. however, I soon realised this was not necessary as the loop.exe booted in the correct manner as intended. 

So the file opencmd is now redundant, however, I have left it in as a reminder to myself of how the windows command line can be run from a python file.


#### The users goals of this program are:
* Automatically test for an internet connection.
* Only run the desired program if a network connection established..
* Visual representation of what is happening.



#### I think this program gives this to the user because:
* The program automatically runs on startup.
* Only if a connection is detected will the desired program be booted.
* The user can see what is going on in the terminal window.

<div align="center">
<img src="https://github.com/jonathanw82/network_test/blob/main/images/network.gif" alt="program gif" width="50%"/></div>

## Credit:

loop.py

https://docs.python.org/3/howto/sockets.html

https://www.youtube.com/watch?v=H5xpMj_-vAo

https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi

opencmd.py

https://stackoverflow.com/questions/46873212/python-to-close-own-cmd-shell-window-on-exit
