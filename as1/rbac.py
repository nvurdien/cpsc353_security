#!/usr/bin/python
"""
sp00ky skelet0n
"""
import sys

def main():
    with open(sys.argv[1]) as g, open(sys.argv[2]) as r, open(sys.argv[3]) as a:
        g = parse_groups(g)
        r = parse_acl(r)

        pass

def parse_acl(acl):
    pass

def parse_groups(g):
    for l in g:
        

    return dict([v,k] for k,v in g.iteritems())

def usage(script):
    print("USAGE: %s groups resources actions" % script)
    sys.exit()

if __name__=="__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
    main()


