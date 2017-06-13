#!/usr/bin/env python
import string

payload = ''.join([x * 4 for x in string.ascii_uppercase])

print payload[:-32]

