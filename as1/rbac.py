#!/usr/bin/python
"""
sp00ky skelet0n
"""
import sys, collections

def main():
    with open(sys.argv[1],'rb') as g:
        g = parse_groups(g)

    with open(sys.argv[2],'rb') as acl:
        acl = parse_acl(acl)

def parse_acl(acl):
    pass

def parse_groups(g):
    d = collections.defaultdict(list)
    for l in g:
        # parse dem colons, yo


        d[group] = members
        

    #return dict([v,k] for k,v in d.iteritems())

def usage(script):
    print("USAGE: %s groups resources actions" % script)
    sys.exit()

if __name__=="__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
    main()


