<h1>ASCII-UNICODE-Converter</h1>

<h3>This is a basic ascii to unicode converter for Malayalam. </h3>

Dependencies:<br>
	* Python 3

Step:<br>
The two python files contain functions to convert malayalam fonts implied by their file names.
<br>
file.txt is a text file containing the list of almost all ascii fonts available in malayalam language, appended with a number that indicates the mapfile number. This number is used to select the appropriate mapping file required for the operation.
<br>
For both the operations, the function to be called is *convert(text,font_name)* from the appropriate python file. For both these functions , the common arguments are: <br>
	- text : the text that require to be converted<br>
	- font_name : font_name as in the exact format as in file.txt(along with mapping data)
<br><br>
You could create a UI for this whole step like this deployed for ICFOSS Trivandrum, http://mlconverter.icfoss.org/ .
<br>
<h3>Licensed under GNU GPL v3.0.</h3>
