import os

'''
Start the windows command prompt.
/k carries out the command specified by string and continues.
color 0A changed the cmd color to green.
Each ampersand must be escaped here with escape character of Windows
command interpreter which is the caret character ^. This is necessary
as otherwise && would be interpreted by first command process running
start as additional command to run after successful execution of start.
Runs the file,
Exits and closes the command line.
'''
os.system("start cmd.exe /k color 0A ^&^& loop.exe ^&^& exit")
