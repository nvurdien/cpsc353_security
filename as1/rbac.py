#!/usr/bin/python
"""
sp00ky skelet0n
"""
import sys, collections

def main():
    with open(sys.argv[1],'rb') as g:
        g = parse_groups(g)
        print(g)

    with open(sys.argv[2],'rb') as acl:
        acl = parse_acl(acl)

def parse_acl(acl):
    pass

def parse_groups(g):
    d = collections.defaultdict(list)
    for l in g:
        l = l.strip()
        if any(l): 
            group, members = l.split(":");
            members = members.split(",")
            members = [x.strip() for x in members]
            d[group] = members
    inv_d = collections.defaultdict(list) 
    for key, values in d.iteritems():
        for value in values:
            inv_d[value].append(key)
    return inv_d

def usage(script):
    print("USAGE: %s groups resources actions" % script)
    sys.exit()

if __name__=="__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
    main()
