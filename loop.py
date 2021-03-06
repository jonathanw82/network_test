import os
import socket
import time


# Change the terminal and CMD.exe color to green
os.system('color 0A')


# File to be booted only if an established network connection detected
bootfile = "C:/Program Files (x86)/touchjams/touchjams.exe"
countdown = 11


# This function adds the dots to the loading lines depending on type
def trailingDots(mode):
    if mode == 'loading':
        loading = '..........'
        for i in range(10):
            print(loading[i], sep='', end='', flush=True)
            time.sleep(0.3)
    elif mode == 'stopping':
        stopping = '....................'
        for i in range(20):
            print(stopping[i], sep='', end='', flush=True)
            time.sleep(0.3)


# Program heading
print("\nChecking For Internet Connection\n")


# Main loop
for x in range(10):
    try:
        # Create a connect to the web server on http port 80
        socket.create_connection(('Google.com', 80))
        # Declare the no connection variable
        noconnection = None
        # Assign the variable noconnection to the exception
    except Exception as noconnection:
        pass
        if noconnection:
            print('LOADING', end='')
            # Add the trailing dots to the inline print statment with end=''
            trailingDots('loading')
            countdown -= 1
            print('', countdown, 'No Connection')
            time.sleep(2)
            continue  # Do the loop again
    else:
        print('LOADING', end='')
        trailingDots('loading')
        print('Connection Established!!!!')
        time.sleep(1)
        print('Booting Jukebox Please wait!')
        # File to be booted on successful detection of internet
        os.startfile(bootfile)
        time.sleep(8)
        break  # Exit the loop and and the program will stop
else:
    print('\nNo Internet Connection', end='')
    trailingDots('loading')
    time.sleep(2)
    print('\nSTOPPING', end='')
    trailingDots('loading')
    time.sleep(2)
    print('\nConnection Check Stopped')
    time.sleep(2)
    print('\nSystem Rebooting!', end="")
    trailingDots('stopping')
    time.sleep(4)
    os.system("shutdown /r /t 1")
