#Name: Sohail Bakhshi 
#Student ID - 20605126
#to run script type bash testKeyMeUp.sh
#!/bin/bash

#testing command line

#test with invalid arguments to see if usage is displayed
python3 keyMeUp.py -a a a a
#test with invalid arguments to see if usage is displayed
python3 keyMeUp.py -a
#testing if interactive mode works
python3 keyMeUp.py -i
#test silent mode works
python3 keyMeUp.py -s keyboard.txt stringfile.txt testoutput.txt
#testing error handling works
python3 keyMeUp.py -s nofile.txt stringfile.txt test.txt