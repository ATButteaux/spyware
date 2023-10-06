dOTP.py is a script that implements a protocol for a pen and paper pseudo random number generator.

The script first converts a text string/row to decimal numbers. The next row of numbers is generated
by a combination of lagged finonachi, addition modulus 10, and a function to split/reorder the previous string.

The result is a pseudo random string of numbers, formatted in the traditional 5 digit groups, for use
in a One Time Pad cipher.

Directions for doing the process with pen and paper to follow soon.

codebook.py is a script that will output a character/decimal converter, a codebook, and a OTP. This data can be imported into a word processing document (formatted with 3 columns, 10pt type) and folded/cut down and stapled into a spy codebook. You can add your own additions to your codebook in your own codebook*.txt file.
