#Import re


#re.match(r'x','x y z')
	-> it will search the string only at the begining

#re.search(pattern, string)
	-> it will search in the whole string for a match
	ex: re.search(r'y', 'x y z')
*Note: It will return only first occurence of the string

#re.findall(pattern, string)
	-> it helps to get a list of all matching patterns
	ex: result = re.findall(r'AV', 'AV Analytics vidhya AV')
	    print result
	output:
		['AV', 'AV']

#re.split(pattern, string, [maxsplit=0]);
	-> this method helps to split string by the occurences of given pattern
	ex: result = re.split(r't', 'Software)
	    print result
	Output:
		['Sof', 'ware']

* we can also give the value to "maxsplit" argument (default value = 0)
	ex: result = re.split(r't', 'Software Task study', maxsplit=1)
	    print result
	Output:
		['Sof', 'ware Task study]

#re.sub(pattern, repl, string)
	-> it helps to serach  a pattern and replace with a new sub string.
	-> if the string is not found , string is returned unchanged.
	ex: result=re.sub(r'India','the World','AV is largest Analytics community of India')
	    print result
	Output:
		'AV is largest Analytics community of the World'

#re.compile(pattern, repl, string):
	-> we can combine a regular expression pattern into pattern objects, which can be
	   used for pattern matching.
	ex: pattern=re.compile('AV')
	    result=pattern.findall('AV Analytics Vidhya AV')
	    print result
	    result2=pattern.findall('AV is largest analytics community of India')
	    print result2 
	Output:
		['AV', 'AV']
	        ['AV']


### Most commonly used OPERATORS:
	->the most commonly used operators that helps to generate an 
	   expression to represent required characters in a string or file

Operators		Description
.	 	Matches with any single character except newline ‘\n’.
?	 	match 0 or 1 occurrence of the pattern to its left
+	 	1 or more occurrences of the pattern to its left
*	 	0 or more occurrences of the pattern to its left
\w	 	Matches with a alphanumeric character whereas \W (upper case W) matches non alphanumeric character.
\d	  	Matches with digits [0-9] and /D (upper case D) matches with non-digits.
\s	 	Matches with a single white space character (space, newline, return, tab, form) and \S (upper case S) matches any non-white space character.
\b	 	boundary between word and non-word and /B is opposite of /b
[..]	 	Matches any single character in a square bracket and [^..] matches any single character not in square bracket
\	 	It is used for special meaning characters like \. to match a period or \+ for plus sign.
^ and $	 	^ and $ match the start or end of the string respectively
{n,m}	 	Matches at least n and at most m occurrences of preceding expression if we write it as {,m} then it will return at least any minimum occurrence to max m preceding expression.
a| b	 	Matches either a or b
( )		Groups regular expressions and returns matched text
\t, \n, \r	 Matches tab, newline, return

**Link:
"https://docs.python.org/2/library/re.html"


Shorthand character class

Represents

\d

Any numeric digit from 0 to 9.

\D

Any character that is not a numeric digit from 0 to 9.

\w

Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

\W

Any character that is not a letter, numeric digit, or the underscore character.

\s

Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S

Any character that is not a space, tab, or newline.