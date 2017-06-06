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
        print(acl)

    with open(sys.argv[3],'rb') as a:
        pass

def parse_acl(acl):
    d = collections.defaultdict(lambda: collections.defaultdict(list))
    key = ''
    for l in acl:
        if not l.startswith(' '):
            key = l.strip().strip(':')
        else:
            l = l.strip()
            if any(l):
                group, members = clean_line(l)
                d[key][group] = members
    return d

def parse_groups(g):
    d = collections.defaultdict(list)
    for l in g:
        l = l.strip()
        if any(l): 
            group, members = clean_line(l)
            d[group] = members
    inv_d = collections.defaultdict(list) 
    for key, values in d.iteritems():
        for value in values:
            inv_d[value].append(key)
    return inv_d

def clean_line(line):
    group, members = line.split(":")
    members = members.split(",")
    members = [x.strip() for x in members]
    return group, members

def usage(script):
    print("USAGE: %s groups resources actions" % script)
    sys.exit()

if __name__=="__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
    main()
