# gcode-belt-Y0-fix
Most belt slicers do print the lowest lines above the belt, this aims to fix that

This scripts finds the lowest Y coordinate in your gcode and shifts down the rest of the gcode by that amount. It uses markers to find the start and end of your part and ignores the start and end gcode.

Prerequisites:
Python
Ideamaker

Setup: 
1. In ideamaker add ";end of Start GCode"(without the quotation marks) to the very end of your start gcode.
2. Add ";end of Gcode" to the very start of your End Gcode
3. Add "python \<path to main.py\> {gcode_file_full_path}" to post processing in the External Terminal Command section
4. Done
