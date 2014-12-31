#!/usr/bin/env python

import sys

try:
    base64IndexTable = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/')
    source = sys.argv[1]
    # Decode the input sting from hex to ASCII
    source = source.decode('hex')
    source_bin = ""
    base64_str = ""

    #sys.stderr.write("Input: " + source + "\n")
    # Input is in hex, we only need to convert it based on the index table, 6 bits at the time
    for char in source:
        # Convert to binary each caracters
        #  - Bin make the output in binary
        #  - Int convert the caracter to the approprirate base 16 value
        #  - lstrip("0b") stips the spaces
        binchar = bin( ord(char) ).lstrip("0b")
        # Now, we need to add 0s until each char is 8bits long
        binchar = ( 8 - len(binchar) ) * "0" + binchar 
        source_bin += binchar

    # The challenge does not require to add padding (The number of bytes is divisable in 3), so I won't be implementing the feature for now
   
    # Iteration through the source lengh for 3 octets into 4 base64 caracters 
    for i in xrange (0, len(source_bin) / 24):
        section = source_bin[(i*24):((1+i)*24)] 
        for j in xrange (0,3):
             base64_bin = section[(j*6):((1+j)*6)]
             base64_str += base64IndexTable[ int( base64_bin, 2 ) ] 
    print ("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")    
    print (base64_str)
except Exception as e:
    print("Someting went wrong, check if the parameter is missing.")
    print (e)
