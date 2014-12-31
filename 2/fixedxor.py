#!/usr/bin/env python

import sys

againts="686974207468652062756c6c277320657965"

try:
    source = sys.argv[1]
    # Use the base 16 as input and do the xor
    r = int(source, 16) ^ int(againts, 16)
    # Strip the 2 first caracter (0x, to indicate this is an hex) 
    # Also stip the last catacter (L) to indicate this is a Long integer 
    print ( hex(r)[2:].rstrip('L') )
except Exception as e:
    print ("Someting went wrong")
    print (e)
