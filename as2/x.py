#!/usr/bin/env python
import sys
import string

shellcode = ''.join([x*4 for x in string.ascii_uppercase])


if len(sys.argv) == 1:
    numberr = 256
else:
    numberr = int(sys.argv[1])

shellcode = 276 * 'A'
print shellcode
