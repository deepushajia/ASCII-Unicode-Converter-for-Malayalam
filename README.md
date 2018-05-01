ASCII-UNICODE-Converter

This is a basic ascii to unicode converter for Malayalam. 

Dependencies:
	* Python 3

Step:
The two python files contain functions to convert malayalam fonts implied by their file names.

file.txt is a text file containing the list of almost all ascii fonts available in malayalam language, appended with a number that indicates the
mapfile number. This number is used to select the appropriate mapping file required for the operation.

For both the operations, the function to be called is *convert(text,font_name)* from the appropriate python file. For both these functions , the 
common arguments are: 
	- text : the text that require to be converted
	- font_name : font_name as in the exact format as in file.txt(along with mapping data)

You could create a UI for this whole step which will soon be deployed for ICFOSS, Trivandrum.

Licensed under GNU GPL v3.0.
