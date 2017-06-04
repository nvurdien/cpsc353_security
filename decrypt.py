#!/usr/bin/env python

import sys
import string

def main(filename):
    with open(filename) as f:
        for cleartext in f:
            ascii = map(ord, cleartext.rstrip('\n'))
            cipher = [c-1 for c in ascii]
            ciphertext = map(chr, cipher)
            print string.join(ciphertext, '')

def usage(scriptname):
    msg = 'Usage: %s FILE' % scriptname
    sys.exit(msg)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage(sys.argv[0])
    main(sys.argv[1])
